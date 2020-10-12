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

namespace GraphicalDesigner_v2._0
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

        //choosing drawing mode
        private void DrawingModeSelection(object sender, RoutedEventArgs e)
        {
            Ink.EditingMode = InkCanvasEditingMode.Ink;
        }

        private void DeletingModeSelection(object sender, RoutedEventArgs e)
        {
            Ink.EditingMode = InkCanvasEditingMode.EraseByStroke;
        }

        private void FormatingModeSelection(object sender, RoutedEventArgs e)
        {
            Ink.EditingMode = InkCanvasEditingMode.Select;
        }

        //choosing brush color
        private void ColorsList_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            if(ColorsList.SelectedIndex == 0)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(255, 255, 255);
            }
            else if(ColorsList.SelectedIndex == 1)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(0, 0, 0);
            }
            else if(ColorsList.SelectedIndex == 2)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(255, 0, 0);
            }
            else if(ColorsList.SelectedIndex == 3)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(255, 128, 0);
            }
            else if(ColorsList.SelectedIndex == 4)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(255, 255, 0);
            }
            else if(ColorsList.SelectedIndex == 5)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(0, 255, 0);
            }
            else if(ColorsList.SelectedIndex == 6)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(0, 255, 255);
            }
            else if(ColorsList.SelectedIndex == 7)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(0, 0, 255);
            }
            else if(ColorsList.SelectedIndex == 8)
            {
                Ink.DefaultDrawingAttributes.Color = Color.FromRgb(128, 0, 128);
            }
        }

        //choosing brush width
        private void BrushWidthChange(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            Ink.DefaultDrawingAttributes.Width = ChooseWidth.Value;
            Ink.DefaultDrawingAttributes.Height = ChooseWidth.Value;
        }
    }
}
