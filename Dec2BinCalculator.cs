using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Dec2BinCalculator
{
    public partial class Form1 : Form
    {

        int[] binaryValues = { 1, 2, 4, 8, 16, 32, 64, 128, 256 };
        Random random = new Random();
        List<ComboBox> comboBoxes = new List<ComboBox>();
        int total;
        int questionNumber;

        Label lblTotal = new Label();
        Label question = new Label();
        Label header = new Label();



        public Form1()
        {
            InitializeComponent();

            LoadGame();
        }


        private void LoadGame()
        {
            Array.Reverse(binaryValues);

            questionNumber = 12;

            this.BackColor = Color.FromArgb(64, 64, 64);

            this.Size = new Size(600, 383);

            //adding header label

            header.Text = "binary calculator game " + Environment.NewLine + "by me :)";
            header.AutoSize = false;
            header.Width = this.ClientSize.Width;
            header.Height = 70;
            header.TextAlign = ContentAlignment.MiddleCenter;
            header.ForeColor = Color.White;
            header.Font = new Font("Arial", 12);
            this.Controls.Add(header);

            //end of header

            //add questions label

            question.Text = "what is - " + questionNumber + " - in binary?";
            question.AutoSize = false;
            question.Width = this.ClientSize.Width;
            question.Height = 50;
            question.TextAlign = ContentAlignment.MiddleCenter;
            question.Font = new Font("Arial", 20);
            question.Top = 180;
            question.ForeColor = Color.LightGreen;
            this.Controls.Add(question);

            // end of question label

            //add total label

            lblTotal.Text = "total: " + total;
            lblTotal.AutoSize = false;
            lblTotal.Width = this.ClientSize.Width;
            lblTotal.Height = 50;
            lblTotal.TextAlign = ContentAlignment.MiddleCenter;
            lblTotal.ForeColor = Color.White;
            lblTotal.Font = new Font("Arial", 20);
            lblTotal.Top = 230;
            this.Controls.Add(lblTotal);

            // end total label

            // comboboxes loops

            int x = 30;
            int y = 120;

            for (int i = 0; i < 9; i++)
            {
                ComboBox box = new ComboBox();

                box.Width = 50;
                box.Items.Add("0");
                box.Items.Add("1");
                box.SelectedIndex = 0;
                box.Font = new Font("Arial", 16);
                box.DropDownStyle = ComboBoxStyle.DropDownList;
                box.Tag = binaryValues[i].ToString();
                box.Left = x;
                box.Top = y;   
                box.FlatStyle = FlatStyle.Flat;
                box.SelectionChangeCommitted += Box_SelectionChangeCommitted;
                comboBoxes.Add(box);
                // end of the combo boxes

                Label lblVal = new Label();
                lblVal.Text = binaryValues[i].ToString();
                lblVal.Font = new Font("Arial", 20);
                lblVal.Location = new Point(x, y - 32);
                lblVal.AutoSize = false;
                lblVal.Width = 50;
                lblVal.Height = 30;

                Color c = Color.FromArgb(random.Next(200, 255), random.Next(150, 255), random.Next(150, 255));

                lblVal.BackColor = c;
                lblVal.ForeColor = Color.Black;
                lblVal.TextAlign = ContentAlignment.MiddleCenter;

                this.Controls.Add(box);
                this.Controls.Add(lblVal);

                x += 60;


            }
        }

        private void Box_SelectionChangeCommitted(object sender, EventArgs e) 
        {
            throw new NotImplementedException();
        }

        private void ResetGame()
        {

        }
    
    }
}
