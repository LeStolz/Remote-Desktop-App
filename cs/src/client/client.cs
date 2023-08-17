using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Net;
using System.Net.Sockets;
using System.IO;
namespace client
{
    public partial class client : Form
    {
        public client()
        {
            InitializeComponent();
        }

        private void butApp_Click(object sender, EventArgs e)
        {
            if (Program.client == null)
            {
                MessageBox.Show("Chưa kết nối đến server");
                return;
            }
            String s = "APPLICATION";
            Program.nw.WriteLine(s); Program.nw.Flush();
            listApp viewApp = new listApp();
            viewApp.ShowDialog();
        }

        private void butConnect_Click(object sender, EventArgs e)
        {
            string s;
            
            bool test = true;
            try
            {
                IPEndPoint ipServer = new IPEndPoint(IPAddress.Parse(txtIP.Text), 5656);
                Program.client = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp);
                Program.client.Connect(ipServer);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Lỗi kết nối đến server");
                test = false;
                Program.client = null;
            }
            if (test)
            {
                MessageBox.Show("Kết nối đến server thành công");
                Program.ns = new NetworkStream(Program.client);
                Program.nr = new StreamReader(Program.ns);
                Program.nw = new StreamWriter(Program.ns);
            }
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (Program.client==null)
            {
                MessageBox.Show("Chưa kết nối đến server");
                return;
            }
            String s = "SHUTDOWN";
            Program.nw.WriteLine(s);Program.nw.Flush();
            Program.client = null;
            
        }

        private void butReg_Click(object sender, EventArgs e)
        {
            if (Program.client==null)
            {
                MessageBox.Show("Chưa kết nối đến server");
                return;
            }
            String s = "REGISTRY";
            Program.nw.WriteLine(s);Program.nw.Flush();
            registry viewApp = new registry();
            viewApp.ShowDialog();
        }

        private void butExit_Click(object sender, EventArgs e)
        {
            
            String s = "QUIT";
            if (Program.client != null)
            {
                Program.nw.WriteLine(s); Program.nw.Flush();
            }
            Application.Exit();
        }

        private void butPic_Click(object sender, EventArgs e)
        {
            if (Program.client==null)
            {
                MessageBox.Show("Chưa kết nối đến server");
                return;
            }
            String s = "TAKEPIC";
            Program.nw.WriteLine(s);Program.nw.Flush();
            pic ViewApp = new pic();
            ViewApp.lam();
            ViewApp.ShowDialog();
            
        }

        private void butKeyLock_Click(object sender, EventArgs e)
        {
            if (Program.client == null)
            {
                MessageBox.Show("Chưa kết nối đến server");
                return;
            }
            String s = "KEYLOG";
            Program.nw.WriteLine(s);Program.nw.Flush();
            keylog ViewApp = new keylog();
            ViewApp.ShowDialog();
        }

        private void client_Closing(object sender, FormClosingEventArgs e)
        {
            String s = "QUIT";
            if (Program.client != null)
            {
                Program.nw.WriteLine(s); Program.nw.Flush();
            }
        }

        private void butProcess_Click(object sender, EventArgs e)
        {
            if (Program.client == null)
            {
                MessageBox.Show("Chưa kết nối đến server");
                return;
            }
            String s = "PROCESS";
            Program.nw.WriteLine(s); Program.nw.Flush();
            process viewApp = new process();
            viewApp.ShowDialog();
        }
    }
}
