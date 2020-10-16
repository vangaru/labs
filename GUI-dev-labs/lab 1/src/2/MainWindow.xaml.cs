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
            ComboBoxItem selectedItem = (ComboBoxItem)(ColorsList.SelectedValue);
            string value = (string)(selectedItem.Content);
            Ink.DefaultDrawingAttributes.Color = (Color)ColorConverter.ConvertFromString(value);
        }

        //choosing brush width
        private void BrushWidthChange(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            Ink.DefaultDrawingAttributes.Width = ChooseWidth.Value;
            Ink.DefaultDrawingAttributes.Height = ChooseWidth.Value;
        }

        private void CloseWindow_Click(object sender, RoutedEventArgs e)
        {
            Close();
        }
    }
}
