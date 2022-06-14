{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6327c3b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: opencv-python in c:\\programdata\\anaconda3\\lib\\site-packages (4.5.5.64)\n",
      "Requirement already satisfied: numpy>=1.14.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from opencv-python) (1.21.5)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: numpy in c:\\programdata\\anaconda3\\lib\\site-packages (1.21.5)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: pandas in c:\\programdata\\anaconda3\\lib\\site-packages (1.4.2)\n",
      "Requirement already satisfied: python-dateutil>=2.8.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2.8.2)\n",
      "Requirement already satisfied: numpy>=1.18.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (1.21.5)\n",
      "Requirement already satisfied: pytz>=2020.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2021.3)\n",
      "Requirement already satisfied: six>=1.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: panel in c:\\programdata\\anaconda3\\lib\\site-packages (0.13.0)\n",
      "Requirement already satisfied: markdown in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (3.3.4)\n",
      "Requirement already satisfied: pyct>=0.4.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (0.4.6)\n",
      "Requirement already satisfied: requests in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (2.27.1)\n",
      "Requirement already satisfied: param>=1.12.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (1.12.0)\n",
      "Requirement already satisfied: bleach in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (4.1.0)\n",
      "Requirement already satisfied: pyviz-comms>=0.7.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (2.0.2)\n",
      "Requirement already satisfied: bokeh<2.5.0,>=2.4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (2.4.2)\n",
      "Requirement already satisfied: tqdm>=4.48.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (4.64.0)\n",
      "Requirement already satisfied: pillow>=7.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (9.0.1)\n",
      "Requirement already satisfied: numpy>=1.11.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (1.21.5)\n",
      "Requirement already satisfied: Jinja2>=2.9 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (2.11.3)\n",
      "Requirement already satisfied: packaging>=16.8 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (21.3)\n",
      "Requirement already satisfied: tornado>=5.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (6.1)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (4.1.1)\n",
      "Requirement already satisfied: PyYAML>=3.10 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (6.0)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\programdata\\anaconda3\\lib\\site-packages (from Jinja2>=2.9->bokeh<2.5.0,>=2.4.0->panel) (2.0.1)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from packaging>=16.8->bokeh<2.5.0,>=2.4.0->panel) (3.0.4)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from tqdm>=4.48.0->panel) (0.4.4)\n",
      "Requirement already satisfied: webencodings in c:\\programdata\\anaconda3\\lib\\site-packages (from bleach->panel) (0.5.1)\n",
      "Requirement already satisfied: six>=1.9.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from bleach->panel) (1.16.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->panel) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->panel) (3.3)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->panel) (2.0.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->panel) (1.26.9)\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n",
      "WARNING: Ignoring invalid distribution -ywinpty (c:\\programdata\\anaconda3\\lib\\site-packages)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Launching server at http://localhost:61516\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<bokeh.server.server.Server at 0x2338f48ed60>"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import os\n",
    "os.sys.path\n",
    "\n",
    "# Installing libraries\n",
    "!pip3 install opencv-python\n",
    "!pip3 install numpy\n",
    "!pip3 install pandas\n",
    "!pip3 install panel\n",
    "\n",
    "# Importing\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from matplotlib.figure import Figure\n",
    "import panel as pn\n",
    "from panel.interact import interact\n",
    "import param\n",
    "import matplotlib.pyplot as plt\n",
    "import hvplot.pandas\n",
    "pn.extension()\n",
    "\n",
    "\n",
    "# Reading Excel files and creation of different Dfs\n",
    "df = pd.read_excel(r\"C:\\Users\\Keithon\\Desktop\\Capstone\\Data\\Test.xlsx\",sheet_name='WorkstageRecordItem')\n",
    "df1 = pd.read_excel(r\"C:\\Users\\Keithon\\Desktop\\Capstone\\Data\\Test.xlsx\",sheet_name='JobCost')\n",
    "df2 = pd.read_excel(r\"C:\\Users\\Keithon\\Desktop\\Capstone\\Data\\Test.xlsx\",sheet_name='JobOrder')\n",
    "\n",
    "df = df.drop(columns =[\"Id\",\"JobOrderId\",\"Status\",\"Reference\",\"TechnicianSignature_StampNo\",\"ApproverRole\",\"ReleaseToSignatorySignature_StampNo\",\"TechnicianSignature_SignedOn\",\"CompletedByUserId\",\"CompletedByFullname\",\"ApprovedByUserId\",\"ApprovedByFullname\",\"ApprovedOn\",\"ReleaseToSignatorySignature_DigitalCertificateId\",\"ReleaseToSignatorySignature_Signature\",\"ReleaseToSignatorySignature_SignedByUserId\",\"ReleaseToSignatorySignature_SignedOn\",\"TechnicianSignature_DigitalCertificateId\",\"TechnicianSignature_Signature\",\"TechnicianSignature_SignedByUserId\"], axis = 1)\n",
    "df1 = df1.drop([\"MWC\"], axis = 1)\n",
    "df2 = df2.drop([\"MWC\",\"ReviewerSignature_Signature\",\"ComplianceDeclarationRecord_ReleaseToSignatorySignature_Signature\",\"SignWorkscopeAndCRRBy\",\"WorkScopeId\",\"SignWorkscopeAndCRRBy\",\"TechnicianSignature_StampNo\",\"TechnicianSignature_SignedOn\",\"TechnicianSignature_SignedByUserId\",\"TechnicianSignature_Signature\",\"TechnicianSignature_DigitalCertificateId\",\"ReviewerSignature_StampNo\",\"ReviewerSignature_SignedOn\",\"ReviewerSignature_SignedByUserId\",\"ReviewerSignature_DigitalCertificateId\",\"ComplianceDeclarationRecord_TechnicianSignature_StampNo\",\"ComplianceDeclarationRecord_ReleaseToSignatorySignature_StampNo\",\"ComplianceDeclarationRecord_TechnicianSignature_SignedOn\",\"ComplianceDeclarationRecord_TechnicianSignature_SignedByUserId\",\"ComplianceDeclarationRecord_TechnicianSignature_Signature\",\"ComplianceDeclarationRecord_TechnicianSignature_DigitalCertificateId\",\"ComplianceDeclarationRecord_ReleaseToSignatorySignature_SignedOn\",\"ComplianceDeclarationRecord_ReleaseToSignatorySignature_SignedByUserId\",\"ComplianceDeclarationRecord_ReleaseToSignatorySignature_DigitalCertificateId\",\"RowVersion\",\"ComplianceDeclarationRecord_ReviewStatus\",\"ComplianceDeclarationRecord_LastDeclaredOn\",\"RejectReason\",\"ComplianceDeclarationRecord_LastDeclaredByUserId\",\"ComplianceDeclarationRecord_LastDeclaredByFullName\",\"ComplianceDeclarationRecord_LastApprovedOn\",\"ComplianceDeclarationRecord_LastApprovedByUserId\",\"ComplianceDeclarationRecord_LastApprovedByFullName\",\"ComplianceDeclarationRecord_IsDeclared\",\"ReviewedBy\",\"NSN\",\"SignWorkscopeAndCRRSignature_DigitalCertificateId\",\"TechnicianSignature_StampNo\",\"MPGType\",\"SignWorkscopeAndCRRSignature_Signature\",\"SignWorkscopeAndCRRSignature_SignedByUserId\",\"SignWorkscopeAndCRRSignature_SignedOn\",\"SignWorkscopeAndCRRSignature_StampNo\"], axis = 1)\n",
    "\n",
    "# Seperation of date and time\n",
    "df['Dates'] = pd.to_datetime(df['CompletedOn'], format = '%Y%m%d').dt.date\n",
    "df['Time'] = pd.to_datetime(df['CompletedOn'], format = '%H%m%s').dt.time\n",
    "\n",
    "# Sorting Values based on Job Order Number\n",
    "df = df.sort_values(by=['JobOrderNo','Sequence'], ascending = True)\n",
    "df1 = df1.rename(columns ={'JobOrder':'JobOrderNo'})\n",
    "\n",
    "#Merging Excel Sheets based on Job Order Number\n",
    "df3 = pd.merge(df, df1, left_on= 'JobOrderNo', right_on ='JobOrderNo')\n",
    "df4 = pd.merge(df3,df2, left_on = 'JobOrderNo', right_on = 'JobOrderNo')\n",
    "\n",
    "\n",
    "# Creating new dfs\n",
    "df1 = pd.read_excel(r\"C:\\Users\\Keithon\\Desktop\\Capstone\\Data\\Test.xlsx\",sheet_name='JobCost')\n",
    "Cost_df = df1.drop(['JobOrder','MWC','PartDesc','Strtmlfn','Malfend','Aircraft','HrClocked'], axis = 1)\n",
    "Total_Part_Number_Avail = list(Cost_df['PartNo'].unique())\n",
    "Total_Work_Req_Avail = list(Cost_df['WorkReq'].unique())\n",
    "\n",
    "# Setting up for Time\n",
    "df1 = pd.read_excel(r\"C:\\Users\\Keithon\\Desktop\\Capstone\\Data\\Test.xlsx\",sheet_name='JobCost')\n",
    "Time_df = df1.drop(['JobOrder','SerialNo','MWC','PartDesc','Aircraft','ActTotCost','ActMatCost','ActLabCost','ActSubcCost','ActOthCost'], axis = 1)\n",
    "New_Rows = []\n",
    "\n",
    "Time_df['Difference'] = (Time_df['Malfend'] - Time_df['Strtmlfn']).dt.days\n",
    "\n",
    "# Removing Start and end dates\n",
    "Time_df = Time_df.drop(['Strtmlfn','Malfend'],axis = 1)\n",
    "\n",
    "\n",
    "df1 = pd.read_excel(r\"C:\\Users\\Keithon\\Desktop\\Capstone\\Data\\Test.xlsx\",sheet_name='JobCost')\n",
    "Cost_df = df1.drop(['JobOrder','MWC','PartDesc','Strtmlfn','Malfend','Aircraft','HrClocked'], axis = 1)\n",
    "Cost_df = Cost_df.rename(columns ={'ActTotCost':'Total','ActMatCost':'Materials','ActSubcCost':'SubContract','ActLabCost':'Labour','ActOthCost':'Others'})\n",
    "Cost_df = Cost_df[['PartNo','WorkReq','Labour', 'Materials', 'SubContract', 'Others', 'Total']]\n",
    "\n",
    "\n",
    "# Setting up title\n",
    "Title = '##Interactive Dashboard'\n",
    "\n",
    "# Setting up panel widgets\n",
    "Select_X = pn.widgets.Select(name='Part Numbers', options= Total_Part_Number_Avail)\n",
    "Select_Y = pn.widgets.Select(name='Work Required', options= Total_Work_Req_Avail)\n",
    "Select_A = pn.widgets.Select(name='Part Numbers', options= Total_Part_Number_Avail)\n",
    "Select_B = pn.widgets.Select(name='Work Required', options= Total_Work_Req_Avail)\n",
    "\n",
    "# Setting up plot for box\n",
    "@pn.depends(Select_X,Select_Y)\n",
    "def Box_Plot(Select_X,Select_Y):\n",
    "    Box = Cost_df[(Cost_df['PartNo'] == Select_X) & (Cost_df['WorkReq'] == Select_Y)].hvplot.box(title = 'Part Number is:' + str(Select_X) +'\\n'+'Work Performed is:'+str(Select_Y) ,value_label='Costs ($)',xlabel = 'Different Types of Cost',legend = False, width = 1100, height = 700)\n",
    "    return Box\n",
    "\n",
    "\n",
    "# Setting up Mahour tracking\n",
    "@pn.depends(Select_A,Select_B)\n",
    "def Hour_Plot(Select_A,Select_B):\n",
    "    Time_Check = Time_df[(Time_df['PartNo'] == Select_A) & (Time_df['WorkReq'] == Select_B)].hvplot.box(title = 'Part Number is:' + str(Select_A) +'\\n'+'Work Performed is:'+str(Select_B) ,y = 'Difference',ylabel = 'Number of Days',xlabel='Average Turn Around Days',legend = False,width = 500, height = 700)\n",
    "    return Time_Check\n",
    "\n",
    "@pn.depends(Select_A,Select_B)\n",
    "def Day_Plot(Select_A,Select_B):\n",
    "    ManHour = Time_df[(Time_df['PartNo'] == Select_A) & (Time_df['WorkReq'] == Select_B)].hvplot.box(title = 'Part Number is: '+ str(Select_A)+ '\\n' + 'Work Hours',y = 'HrClocked',ylabel = 'Hours',xlabel='ManHour',legend = False, width = 500, height = 700)\n",
    "    return ManHour\n",
    "    \n",
    "# For Manhour tab\n",
    "p2 = pn.Row(\n",
    "        pn.WidgetBox(Title,Select_A,Select_B),\n",
    "        pn.Column(Hour_Plot),\n",
    "        pn.bind(Day_Plot,Select_A,Select_B), name = 'ManHour Tracking')\n",
    "\n",
    "# For Cost tab\n",
    "p1 = pn.Row(\n",
    "        pn.WidgetBox(Title,Select_X,Select_Y),\n",
    "        pn.bind(Box_Plot,Select_X,Select_Y), name = 'Costs')\n",
    "\n",
    "\n",
    "tabs = pn.Tabs(p1,p2, dynamic = True)\n",
    "tabs.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "fe1fd261",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1511482711.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Input \u001b[1;32mIn [11]\u001b[1;36m\u001b[0m\n\u001b[1;33m    ssh -NfL localhost:57871:localhost:57871 Keithon@remote.host\u001b[0m\n\u001b[1;37m             ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
