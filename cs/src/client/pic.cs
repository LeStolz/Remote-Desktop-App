using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
using System.Drawing.Imaging;
namespace client
{
    public partial class pic : Form
    {
        public pic()
        {
            InitializeComponent();
        }
        public void lam()
        {

            String s = "TAKE";
            Program.nw.WriteLine(s);Program.nw.Flush();
            s=Program.nr.ReadLine();
            Byte[] data = new Byte[Convert.ToInt32(s)];
            int rec = Program.client.Receive(data);
            MemoryStream ms = new MemoryStream(data);
            // picScreen.Save(Application.StartupPath+"\\picScreen.Png",ImageFormat.Png);
            //picture.Image = Image.FromFile(Application.StartupPath+"\\picScreen.Png");
            picture.Image= Bitmap.FromStream(ms);

        }

        private void butTake_Click(object sender, EventArgs e)
        {
            lam();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SaveFileDialog save = new SaveFileDialog();

            save.Filter = "Bmp files (*.Bmp)|*.Bmp|All files (*.*)|*.*";
            save.FilterIndex = 2;

            if (save.ShowDialog() == System.Windows.Forms.DialogResult.OK)
            {

                    picture.Image.Save(save.FileName, ImageFormat.Png);

            }
        }

        private void pic_closing(object sender, FormClosingEventArgs e)
        {
            String s = "QUIT";
            Program.nw.WriteLine(s); Program.nw.Flush();
        }
    }
}
