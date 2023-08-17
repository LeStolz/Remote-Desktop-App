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
    public partial class Kill : Form
    {
        public Kill()
        {
            InitializeComponent();
        }

        private void butNhap_Click(object sender, EventArgs e)
        {
            Program.nw.WriteLine("KILLID"); Program.nw.Flush();
            Program.nw.WriteLine(txtID.Text); Program.nw.Flush();
            String s = Program.nr.ReadLine();
            MessageBox.Show(s);
        }

        private void kill_closing(object sender, FormClosingEventArgs e)
        {
            Program.nw.WriteLine("QUIT"); Program.nw.Flush();
        }
    }
}
