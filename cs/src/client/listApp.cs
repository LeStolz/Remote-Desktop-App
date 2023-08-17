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
    public partial class listApp : Form
    {
        public listApp()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string temp = "KILL";
            Program.nw.WriteLine(temp);Program.nw.Flush();
            Kill viewkill = new Kill();
            viewkill.ShowDialog();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string temp = "XEM";
            Program.nw.WriteLine(temp);Program.nw.Flush();
            string s1 = "name application";
            string s2 = "ID";
            string s3 = "count";
            temp=Program.nr.ReadLine();
            int soprocess = Convert.ToInt32(temp);
            int i;
            //reset list?
            for (i = 0; i < soprocess; i++)
            {
                s1 = Program.nr.ReadLine(); 
                if (s1 == "ok")
                {
                    s1 = Program.nr.ReadLine(); 
                    
                    // Thread.Sleep(20);

                    s2 = Program.nr.ReadLine(); 
                    
                    // Thread.Sleep(20);

                    s3 = Program.nr.ReadLine();
                    
                    //Thread.Sleep(20);

                    ListViewItem one = new ListViewItem(new string[] { s1, s2, s3 });
                    listView1.Items.Add(one);
                }

            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string temp = "START";
            Program.nw.WriteLine(temp);Program.nw.Flush();
            Start viewstart = new Start();
            viewstart.ShowDialog();
        }

        private void listApp_closing(object sender, FormClosingEventArgs e)
        {
            String s = "QUIT";
            Program.nw.WriteLine(s); Program.nw.Flush();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (listView1.Items != null)
            {
                foreach (ListViewItem item in listView1.Items)
                {
                    listView1.Items.Remove(item);
                }
            }
        }

    }
}
