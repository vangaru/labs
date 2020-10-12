using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace Graphical_Designer
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Menu_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Menu";
        }

        private void Background_White_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.White;
        }

        private void Background_Red_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.Red;
        }

        private void Background_Yellow_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.Yellow;
        }

        private void Background_Green_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.Green;
        }

        private void Background_Blue_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.Blue;
        }

        private void Background_LightBlue_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.Cyan;
        }

        private void Background_Purple_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.Purple;
        }

        private void Background_Orange_Click(object sender, RoutedEventArgs e)
        {
            MainGrid.Background = Brushes.Orange;
        }

        private void WhiteButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to white";
        }

        private void RedButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to red";
        }


        private void OrangeButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to orange";
        }


        private void GreenButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to green";
        }


        private void LightBlueButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to light blue";
        }

        private void BlueButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to blue";
        }

        private void PurpleButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to purple";
        }

        private void CloseWindow_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }

        private void CloseWindow_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Close the window";
        }

        private void Info_Click(object sender, RoutedEventArgs e)
        {
            MessageBox.Show("My name is Ivanenko Ivan.I am student of the 2'nd course of FEIS.");
        }

        private void Info_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Who is the developer?";
        }

        private void YellowButton_MouseEnter(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "Change background to yellow";
        }

        private void ClearStatusLine(object sender, MouseEventArgs e)
        {
            CurrentStatus.Text = "";
        }
    }
}
