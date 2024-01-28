
using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;

namespace ConsoleTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                new Writer().Run();
                Console.WriteLine("Чтобы пройти еще раз нажмите enter");
                ConsoleKey enter = Console.ReadKey(true).Key;
                Console.Clear();
                if (enter != ConsoleKey.Enter)
                {
                    break;
                }
            }
        }
    }

    class Data
    {
        public int per_minute;
        public string per_second;

        public Data(int per_minute, string per_second)
        {
            this.per_minute = per_minute;
            this.per_second = per_second;
        }
    }

    static class TableRecord
    {
        static string user;

        static public void Login()
        {
            Console.WriteLine("Введите имя:");
            user = Console.ReadLine();
            Console.Clear();
        }

        static public void Save(int symbols)
        {
            Console.Clear();

            if (!File.Exists($@"{Environment.CurrentDirectory}\records.json"))
            {
                File.WriteAllText($@"{Environment.CurrentDirectory}\records.json", "");
            }
            Dictionary<string, Data> result = JsonConvert.DeserializeObject<Dictionary<string, Data>>(File.ReadAllText($@"{Environment.CurrentDirectory}\records.json"));
            if (result == null)
            {
                result = new Dictionary<string, Data>() { };
            }
            result[user] = new Data(symbols, String.Format("{0:f2}", (double)symbols / 60));
            string json = JsonConvert.SerializeObject(result);
            File.WriteAllText($@"{Environment.CurrentDirectory}\records.json", json);
            WriteRecord(result);
        }

        static private void WriteRecord(Dictionary<string, Data> result)
        {
            foreach (string key in result.Keys)
            {
                Data info = result[key];
                Console.WriteLine($"{key}: в минуту - {info.per_minute}, в секунду - {info.per_second}");
            }
            Console.WriteLine();
        }
    }

    public class Writer
    {
        string text = " Наш класс стал бороться за звание \" Самый классный класс\". По всем показателям все хорошо. А вот по патриотическому воспитанию отставали. Нужно было придумать что-то инновационное. Все активисты, отличники, думали, но ничего не приходило им в голову. Витя придумал сшить георгиевскую ленточку размером 50 м, положить ее у Стены Памяти. ( 50 слов)\n";
        int pos_y;
        int cursor = 0;
        Thread thread;

        public Writer() { }

        public void Run()
        {
            TableRecord.Login();
            Console.WriteLine(text);
            Console.WriteLine("___________________");
            Console.WriteLine("Нажмите любую клавишу чтобы начать");

            pos_y = Console.CursorTop + 1;

            Console.ReadKey(true);
            Timer();

            while (thread.IsAlive && cursor < text.Length)
            {
                char key = Console.ReadKey(true).KeyChar;
                if (key == text[cursor])
                {
                    cursor++;
                    Console.ForegroundColor = ConsoleColor.Green;
                    Console.SetCursorPosition(0, 0);
                    Console.Write(text.Substring(0, cursor));
                    Console.ResetColor();
                    Console.WriteLine(text.Substring(cursor));
                }
            }

            if (thread.IsAlive)
            {
                thread.Abort();
            }

            TableRecord.Save(cursor);
        }

        private void Timer()
        {
            thread = new Thread(_ =>
            {
                TimeSpan totalTime = new TimeSpan(0, 0, 1, 0);

                while (totalTime > TimeSpan.Zero)
                {
                    totalTime = totalTime.Subtract(new TimeSpan(0, 0, 0, 1));
                    Console.SetCursorPosition(0, pos_y);
                    Console.WriteLine(totalTime.ToString());

                    Thread.Sleep(1000);
                }
            });

            thread.Start();
        }
    }
}
