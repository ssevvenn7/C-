﻿

using System;

namespace ConsoleApp1
{
    internal class Program
    {

        static void Main(string[] args) { 

            (int,int) Read2Numbers(string msg1= "Введите первое число", string msg2= "Введите второе число")
            {
                Console.WriteLine(msg1);
                int num1 = Convert.ToInt32(Console.ReadLine());
                Console.WriteLine(msg2);
                int num2 = Convert.ToInt32(Console.ReadLine());
                return (num1,num2);

            }

            void getMenu()
            {
                Console.WriteLine();
                Console.WriteLine("__________MENU__________");
                Console.WriteLine("1. Сложить 2 числа");
                Console.WriteLine("2. Вычесть первое из второго");
                Console.WriteLine("3. Перемножить два числа");
                Console.WriteLine("4. Разделить первое на второе");
                Console.WriteLine("5. Возвести в степень N первое число");
                Console.WriteLine("6. Найти квадратный корень из числа");
                Console.WriteLine("7. Найти 1 процент от числа");
                Console.WriteLine("8. Найти факториал из числа");
                Console.WriteLine("9. Выйти из программы");
                Console.WriteLine("________________________");
                Console.WriteLine();
            }

            int factorial(int num)
            {
                int res = 1;
                for(int start = 1;start<=num;++start)
                {
                    res *= start;
                }
                return res;
            }



            int asked;
            do
            {
                getMenu();

                asked = Convert.ToInt32(Console.ReadLine());
                switch (asked)
                    {
                        case 1:
                        {
                            (int, int) numbers = Read2Numbers();

                            int num1 = numbers.Item1, num2 = numbers.Item2;

                            Console.WriteLine($"{num1} + {num2} = {num1 + num2}");
                            break;
                        }

                        case 2:
                        {
                            (int, int) numbers = Read2Numbers();

                            int num1 = numbers.Item1, num2 = numbers.Item2;

                            Console.WriteLine($"{num1} - {num2} = {num1 - num2}");
                            break;
                        }
                    case 3:
                        {
                            (int, int) numbers = Read2Numbers();
                            int num1 = numbers.Item1,num2 = numbers.Item2;

                            Console.WriteLine($"{num1} * {num2} = {num1 * num2}");
                            break;
                        }
                        case 4:
                        {
                            (int, int) numbers = Read2Numbers();
                            int num1 = numbers.Item1, num2 = numbers.Item2;

                            Console.WriteLine($"{num1} / {num2} = {num1 / num2}");
                            break;
                        }
                    case 5:
                        {

                            (int, int) numbers = Read2Numbers("Введите число", "Введите N");
                            int num1 = numbers.Item1, num2 = numbers.Item2;

                            Console.WriteLine($"{num1} ^ {num2} = {Math.Pow(num1,num2)}");
                            break;
                        }
                    case 6:
                        {
                            Console.WriteLine("Введите число");
                            int number = Convert.ToInt32(Console.ReadLine());
                            Console.WriteLine($"Корень числа {number} = {Math.Sqrt(number)}");
                            break;
                        }
                    case 7:
                        {
                            Console.WriteLine("Введите число");
                            int number = Convert.ToInt32(Console.ReadLine());
                            Console.WriteLine($"1 процент от числа {number} = {number*0.01}");
                            break;
                        }
                    case 8:
                        {
                            Console.WriteLine("Введите число");
                            int number = Convert.ToInt32(Console.ReadLine());
                            Console.WriteLine($"Факториал числа {number} = {factorial(number)}");
                            break;
                        }

                }
            }

            while (asked != 9);
        }
    }
}
