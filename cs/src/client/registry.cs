using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.IO;
namespace client
{
  
    public partial class registry : Form
    {
        
        public registry()
        {
            InitializeComponent();
        }

        private void butSend_Click(object sender, EventArgs e)
        {
            String s = "REG";
            Program.nw.WriteLine(s);Program.nw.Flush();    
             s=txtReg.Text;
            Program.nw.Write(s);Program.nw.Flush();
            s=Program.nr.ReadLine();
            MessageBox.Show(s);
        }

        private void folderBrowserDialog1_HelpRequest(object sender, EventArgs e)
        {

        }

        private void butBro_Click(object sender, EventArgs e)
        {
            OpenFileDialog op = new OpenFileDialog();


            op.Filter = "reg file|*.reg";
            if (op.ShowDialog() == DialogResult.OK)
            {
                txtBro.Text = op.FileName;



                StreamReader fin = new StreamReader(txtBro.Text);
                //Byte[] data=new Byte[1024];
                if (fin != null)
                {
                    txtReg.Text = fin.ReadToEnd();
                }
                else MessageBox.Show("Lỗi");
                fin.Close();
            }
        }

        private void comboBox2_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (opApp.Text)
            {
                case "Get value": txtNameValue.Visible = true; txtValue.Visible = false; opTypeValue.Visible = false; break;
                case "Set value": txtNameValue.Visible = true; txtValue.Visible = true; opTypeValue.Visible = true; break;
                case "Delete value": txtNameValue.Visible = true; txtValue.Visible = false; opTypeValue.Visible = false; break;
                case "Create key": txtNameValue.Visible = false; txtValue.Visible = false; opTypeValue.Visible = false; break;
                case "Delete key": txtNameValue.Visible = false; txtValue.Visible = false; opTypeValue.Visible = false; break;
             }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            String s = "SEND";

            Program.nw.WriteLine(s);Program.nw.Flush();
            s = opApp.Text;
            Program.nw.WriteLine(s);Program.nw.Flush();
            s = txtLink.Text;
            Program.nw.WriteLine(s);Program.nw.Flush();
            s = txtNameValue.Text;
            Program.nw.WriteLine(s);Program.nw.Flush();
            s = txtValue.Text;
            Program.nw.WriteLine(s);Program.nw.Flush();
            s = opTypeValue.Text;
            Program.nw.WriteLine(s);Program.nw.Flush();
            s=Program.nr.ReadLine();
            txtKQ.Text += s+"\n";
        }

        private void registry_closing(object sender, FormClosingEventArgs e)
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
