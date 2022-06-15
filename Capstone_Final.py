{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6327c3b4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: opencv-python in c:\\programdata\\anaconda3\\lib\\site-packages (4.5.5.64)\n",
      "Requirement already satisfied: numpy>=1.17.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from opencv-python) (1.21.5)\n"
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
      "Requirement already satisfied: pytz>=2020.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (2021.3)\n",
      "Requirement already satisfied: numpy>=1.18.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from pandas) (1.21.5)\n",
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
      "Requirement already satisfied: bokeh<2.5.0,>=2.4.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (2.4.2)\n",
      "Requirement already satisfied: tqdm>=4.48.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (4.64.0)\n",
      "Requirement already satisfied: pyct>=0.4.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (0.4.6)\n",
      "Requirement already satisfied: markdown in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (3.3.4)\n",
      "Requirement already satisfied: pyviz-comms>=0.7.4 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (2.0.2)\n",
      "Requirement already satisfied: bleach in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (4.1.0)\n",
      "Requirement already satisfied: param>=1.12.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (1.12.0)\n",
      "Requirement already satisfied: requests in c:\\programdata\\anaconda3\\lib\\site-packages (from panel) (2.27.1)\n",
      "Requirement already satisfied: packaging>=16.8 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (21.3)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (4.1.1)\n",
      "Requirement already satisfied: Jinja2>=2.9 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (2.11.3)\n",
      "Requirement already satisfied: pillow>=7.1.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (9.0.1)\n",
      "Requirement already satisfied: numpy>=1.11.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (1.21.5)\n",
      "Requirement already satisfied: PyYAML>=3.10 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (6.0)\n",
      "Requirement already satisfied: tornado>=5.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from bokeh<2.5.0,>=2.4.0->panel) (6.1)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\programdata\\anaconda3\\lib\\site-packages (from Jinja2>=2.9->bokeh<2.5.0,>=2.4.0->panel) (2.0.1)\n",
      "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from packaging>=16.8->bokeh<2.5.0,>=2.4.0->panel) (3.0.4)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from tqdm>=4.48.0->panel) (0.4.4)\n",
      "Requirement already satisfied: six>=1.9.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from bleach->panel) (1.16.0)\n",
      "Requirement already satisfied: webencodings in c:\\programdata\\anaconda3\\lib\\site-packages (from bleach->panel) (0.5.1)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->panel) (3.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->panel) (2021.10.8)\n",
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
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {},
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.holoviews_exec.v0+json": "",
      "text/html": [
       "<div id='1002'>\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "\n",
       "  <div class=\"bk-root\" id=\"5327be2e-7a3f-4199-ab0c-372fd7add62b\" data-root-id=\"1002\"></div>\n",
       "</div>\n",
       "<script type=\"application/javascript\">(function(root) {\n",
       "  function embed_document(root) {\n",
       "    var docs_json = {\"b21307fa-0cdc-4423-910d-79493b062893\":{\"defs\":[{\"extends\":null,\"module\":null,\"name\":\"ReactiveHTML1\",\"overrides\":[],\"properties\":[]},{\"extends\":null,\"module\":null,\"name\":\"FlexBox1\",\"overrides\":[],\"properties\":[{\"default\":\"flex-start\",\"kind\":null,\"name\":\"align_content\"},{\"default\":\"flex-start\",\"kind\":null,\"name\":\"align_items\"},{\"default\":\"row\",\"kind\":null,\"name\":\"flex_direction\"},{\"default\":\"wrap\",\"kind\":null,\"name\":\"flex_wrap\"},{\"default\":\"flex-start\",\"kind\":null,\"name\":\"justify_content\"}]},{\"extends\":null,\"module\":null,\"name\":\"GridStack1\",\"overrides\":[],\"properties\":[{\"default\":\"warn\",\"kind\":null,\"name\":\"mode\"},{\"default\":null,\"kind\":null,\"name\":\"ncols\"},{\"default\":null,\"kind\":null,\"name\":\"nrows\"},{\"default\":true,\"kind\":null,\"name\":\"allow_resize\"},{\"default\":true,\"kind\":null,\"name\":\"allow_drag\"},{\"default\":[],\"kind\":null,\"name\":\"state\"}]},{\"extends\":null,\"module\":null,\"name\":\"click1\",\"overrides\":[],\"properties\":[{\"default\":\"\",\"kind\":null,\"name\":\"terminal_output\"},{\"default\":\"\",\"kind\":null,\"name\":\"debug_name\"},{\"default\":0,\"kind\":null,\"name\":\"clears\"}]},{\"extends\":null,\"module\":null,\"name\":\"TemplateActions1\",\"overrides\":[],\"properties\":[{\"default\":0,\"kind\":null,\"name\":\"open_modal\"},{\"default\":0,\"kind\":null,\"name\":\"close_modal\"}]},{\"extends\":null,\"module\":null,\"name\":\"MaterialTemplateActions1\",\"overrides\":[],\"properties\":[{\"default\":0,\"kind\":null,\"name\":\"open_modal\"},{\"default\":0,\"kind\":null,\"name\":\"close_modal\"}]}],\"roots\":{\"references\":[{\"attributes\":{\"reload\":false},\"id\":\"1281\",\"type\":\"panel.models.location.Location\"},{\"attributes\":{},\"id\":\"1016\",\"type\":\"CategoricalScale\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_alpha\":{\"value\":1.0},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":1.0},\"hatch_color\":{\"value\":\"black\"},\"hatch_scale\":{\"value\":12.0},\"hatch_weight\":{\"value\":1.0},\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1086\",\"type\":\"VBar\"},{\"attributes\":{\"line_alpha\":{\"value\":0.2},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1067\",\"type\":\"Segment\"},{\"attributes\":{},\"id\":\"1120\",\"type\":\"UnionRenderers\"},{\"attributes\":{},\"id\":\"1018\",\"type\":\"LinearScale\"},{\"attributes\":{\"line_alpha\":{\"value\":0.1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1074\",\"type\":\"Segment\"},{\"attributes\":{\"child\":{\"id\":\"1146\"},\"name\":\"ManHour Tracking\",\"title\":\"ManHour Tracking\"},\"id\":\"1147\",\"type\":\"Panel\"},{\"attributes\":{\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1070\",\"type\":\"Segment\"},{\"attributes\":{},\"id\":\"1121\",\"type\":\"Selection\"},{\"attributes\":{\"tools\":[{\"id\":\"1027\"},{\"id\":\"1028\"},{\"id\":\"1029\"},{\"id\":\"1030\"},{\"id\":\"1031\"}]},\"id\":\"1033\",\"type\":\"Toolbar\"},{\"attributes\":{},\"id\":\"1097\",\"type\":\"AllLabels\"},{\"attributes\":{\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1049\",\"type\":\"Segment\"},{\"attributes\":{},\"id\":\"1109\",\"type\":\"Selection\"},{\"attributes\":{\"source\":{\"id\":\"1079\"}},\"id\":\"1085\",\"type\":\"CDSView\"},{\"attributes\":{\"coordinates\":null,\"data_source\":{\"id\":\"1055\"},\"glyph\":{\"id\":\"1057\"},\"group\":null,\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1059\"},\"nonselection_glyph\":{\"id\":\"1058\"},\"selection_glyph\":{\"id\":\"1062\"},\"view\":{\"id\":\"1061\"}},\"id\":\"1060\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"data\":{\"x0\":[[\"Labour\",-0.2],[\"Materials\",-0.2],[\"SubContract\",-0.2],[\"Others\",-0.2],[\"Total\",-0.2]],\"x1\":[[\"Labour\",0.2],[\"Materials\",0.2],[\"SubContract\",0.2],[\"Others\",0.2],[\"Total\",0.2]],\"y0\":[327.0,100.0,99.0,104.0,611.0],\"y1\":[327.0,100.0,99.0,104.0,611.0]},\"selected\":{\"id\":\"1117\"},\"selection_policy\":{\"id\":\"1116\"}},\"id\":\"1071\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"line_alpha\":{\"value\":0.1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1058\",\"type\":\"Segment\"},{\"attributes\":{\"data\":{\"bottom\":{\"__ndarray__\":\"AAAAAABAcUAAAAAAAABZQAAAAAAAkFdAAAAAAADAWUAAAAAAAJ6BQA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]},\"index\":[\"Labour\",\"Materials\",\"SubContract\",\"Others\",\"Total\"],\"top\":{\"__ndarray__\":\"AAAAAAAgbEAAAAAAAABZQAAAAAAAYFZAAAAAAACAWUAAAAAAACSAQA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]}},\"selected\":{\"id\":\"1119\"},\"selection_policy\":{\"id\":\"1118\"}},\"id\":\"1079\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_color\":{\"value\":\"#30a2da\"},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1089\",\"type\":\"VBar\"},{\"attributes\":{\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1062\",\"type\":\"Segment\"},{\"attributes\":{\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1057\",\"type\":\"Segment\"},{\"attributes\":{\"bottom_units\":\"screen\",\"coordinates\":null,\"fill_alpha\":0.5,\"fill_color\":\"lightgrey\",\"group\":null,\"left_units\":\"screen\",\"level\":\"overlay\",\"line_alpha\":1.0,\"line_color\":\"black\",\"line_dash\":[4,4],\"line_width\":2,\"right_units\":\"screen\",\"syncable\":false,\"top_units\":\"screen\"},\"id\":\"1032\",\"type\":\"BoxAnnotation\"},{\"attributes\":{\"coordinates\":null,\"data_source\":{\"id\":\"1071\"},\"glyph\":{\"id\":\"1073\"},\"group\":null,\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1075\"},\"nonselection_glyph\":{\"id\":\"1074\"},\"selection_glyph\":{\"id\":\"1078\"},\"view\":{\"id\":\"1077\"}},\"id\":\"1076\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"line_alpha\":{\"value\":0.2},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1059\",\"type\":\"Segment\"},{\"attributes\":{\"axis\":{\"id\":\"1020\"},\"coordinates\":null,\"grid_line_color\":null,\"group\":null,\"ticker\":null},\"id\":\"1022\",\"type\":\"Grid\"},{\"attributes\":{\"line_alpha\":{\"value\":0.2},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1075\",\"type\":\"Segment\"},{\"attributes\":{\"end\":664.1,\"reset_end\":664.1,\"reset_start\":26.9,\"start\":26.9,\"tags\":[[[\"Costs ($)\",\"Costs ($)\",null]]]},\"id\":\"1010\",\"type\":\"Range1d\"},{\"attributes\":{\"data\":{\"x0\":[[\"Labour\",-0.2],[\"Materials\",-0.2],[\"SubContract\",-0.2],[\"Others\",-0.2],[\"Total\",-0.2]],\"x1\":[[\"Labour\",0.2],[\"Materials\",0.2],[\"SubContract\",0.2],[\"Others\",0.2],[\"Total\",0.2]],\"y0\":[123.0,100.0,80.0,100.0,422.0],\"y1\":[123.0,100.0,80.0,100.0,422.0]},\"selected\":{\"id\":\"1115\"},\"selection_policy\":{\"id\":\"1114\"}},\"id\":\"1063\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.2},\"fill_color\":{\"value\":\"black\"},\"hatch_alpha\":{\"value\":0.2},\"line_alpha\":{\"value\":0.2},\"x\":{\"field\":\"index\"},\"y\":{\"field\":\"Costs_left_parenthesis_right_parenthesis\"}},\"id\":\"1043\",\"type\":\"Circle\"},{\"attributes\":{\"source\":{\"id\":\"1055\"}},\"id\":\"1061\",\"type\":\"CDSView\"},{\"attributes\":{},\"id\":\"1096\",\"type\":\"CategoricalTickFormatter\"},{\"attributes\":{},\"id\":\"1115\",\"type\":\"Selection\"},{\"attributes\":{},\"id\":\"1108\",\"type\":\"UnionRenderers\"},{\"attributes\":{},\"id\":\"1021\",\"type\":\"CategoricalTicker\"},{\"attributes\":{\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1065\",\"type\":\"Segment\"},{\"attributes\":{\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1078\",\"type\":\"Segment\"},{\"attributes\":{\"factors\":[\"Labour\",\"Materials\",\"SubContract\",\"Others\",\"Total\"],\"tags\":[[[\"Variable\",\"Variable\",null]]]},\"id\":\"1009\",\"type\":\"FactorRange\"},{\"attributes\":{\"coordinates\":null,\"data_source\":{\"id\":\"1079\"},\"glyph\":{\"id\":\"1081\"},\"group\":null,\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1083\"},\"nonselection_glyph\":{\"id\":\"1082\"},\"selection_glyph\":{\"id\":\"1086\"},\"view\":{\"id\":\"1085\"}},\"id\":\"1084\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"source\":{\"id\":\"1047\"}},\"id\":\"1053\",\"type\":\"CDSView\"},{\"attributes\":{},\"id\":\"1024\",\"type\":\"BasicTicker\"},{\"attributes\":{\"below\":[{\"id\":\"1020\"}],\"center\":[{\"id\":\"1022\"},{\"id\":\"1026\"}],\"height\":700,\"left\":[{\"id\":\"1023\"}],\"margin\":[5,5,5,5],\"min_border_bottom\":10,\"min_border_left\":10,\"min_border_right\":10,\"min_border_top\":10,\"renderers\":[{\"id\":\"1044\"},{\"id\":\"1052\"},{\"id\":\"1060\"},{\"id\":\"1068\"},{\"id\":\"1076\"},{\"id\":\"1084\"},{\"id\":\"1092\"}],\"sizing_mode\":\"fixed\",\"title\":{\"id\":\"1012\"},\"toolbar\":{\"id\":\"1033\"},\"width\":1100,\"x_range\":{\"id\":\"1009\"},\"x_scale\":{\"id\":\"1016\"},\"y_range\":{\"id\":\"1010\"},\"y_scale\":{\"id\":\"1018\"}},\"id\":\"1011\",\"subtype\":\"Figure\",\"type\":\"Plot\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_alpha\":{\"value\":0.2},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":0.2},\"line_alpha\":{\"value\":0.2},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1091\",\"type\":\"VBar\"},{\"attributes\":{\"coordinates\":null,\"data_source\":{\"id\":\"1047\"},\"glyph\":{\"id\":\"1049\"},\"group\":null,\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1051\"},\"nonselection_glyph\":{\"id\":\"1050\"},\"selection_glyph\":{\"id\":\"1054\"},\"view\":{\"id\":\"1053\"}},\"id\":\"1052\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"coordinates\":null,\"group\":null,\"text\":\"Part Number is:505CH2\\nWork Performed is:REP\",\"text_color\":\"black\",\"text_font_size\":\"12pt\"},\"id\":\"1012\",\"type\":\"Title\"},{\"attributes\":{\"fill_alpha\":{\"value\":0.1},\"fill_color\":{\"value\":\"black\"},\"hatch_alpha\":{\"value\":0.1},\"line_alpha\":{\"value\":0.1},\"x\":{\"field\":\"index\"},\"y\":{\"field\":\"Costs_left_parenthesis_right_parenthesis\"}},\"id\":\"1042\",\"type\":\"Circle\"},{\"attributes\":{},\"id\":\"1100\",\"type\":\"AllLabels\"},{\"attributes\":{},\"id\":\"1113\",\"type\":\"Selection\"},{\"attributes\":{\"axis_label\":\"Costs ($)\",\"coordinates\":null,\"formatter\":{\"id\":\"1099\"},\"group\":null,\"major_label_policy\":{\"id\":\"1100\"},\"ticker\":{\"id\":\"1024\"}},\"id\":\"1023\",\"type\":\"LinearAxis\"},{\"attributes\":{},\"id\":\"1114\",\"type\":\"UnionRenderers\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_color\":{\"value\":\"#30a2da\"},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1081\",\"type\":\"VBar\"},{\"attributes\":{},\"id\":\"1119\",\"type\":\"Selection\"},{\"attributes\":{\"axis_label\":\"Different Types of Cost\",\"coordinates\":null,\"formatter\":{\"id\":\"1096\"},\"group\":null,\"major_label_policy\":{\"id\":\"1097\"},\"ticker\":{\"id\":\"1021\"}},\"id\":\"1020\",\"type\":\"CategoricalAxis\"},{\"attributes\":{\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1054\",\"type\":\"Segment\"},{\"attributes\":{\"axis\":{\"id\":\"1023\"},\"coordinates\":null,\"dimension\":1,\"grid_line_color\":null,\"group\":null,\"ticker\":null},\"id\":\"1026\",\"type\":\"Grid\"},{\"attributes\":{\"source\":{\"id\":\"1039\"}},\"id\":\"1045\",\"type\":\"CDSView\"},{\"attributes\":{\"angle\":{\"value\":0.0},\"fill_alpha\":{\"value\":1.0},\"fill_color\":{\"value\":\"black\"},\"hatch_alpha\":{\"value\":1.0},\"hatch_color\":{\"value\":\"black\"},\"hatch_scale\":{\"value\":12.0},\"hatch_weight\":{\"value\":1.0},\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"size\":{\"value\":4},\"x\":{\"field\":\"index\"},\"y\":{\"field\":\"Costs_left_parenthesis_right_parenthesis\"}},\"id\":\"1046\",\"type\":\"Circle\"},{\"attributes\":{},\"id\":\"1118\",\"type\":\"UnionRenderers\"},{\"attributes\":{\"margin\":[5,10,5,10],\"options\":[\"REP\",\"O/H\",\"SST\"],\"title\":\"Work Required\",\"value\":\"REP\"},\"id\":\"1007\",\"type\":\"panel.models.widgets.CustomSelect\"},{\"attributes\":{\"child\":{\"id\":\"1003\"},\"name\":\"Costs\",\"title\":\"Costs\"},\"id\":\"1145\",\"type\":\"Panel\"},{\"attributes\":{\"children\":[{\"id\":\"1011\"}],\"margin\":[0,0,0,0],\"name\":\"Row02242\"},\"id\":\"1008\",\"type\":\"Row\"},{\"attributes\":{\"line_alpha\":{\"value\":0.1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1050\",\"type\":\"Segment\"},{\"attributes\":{},\"id\":\"1111\",\"type\":\"Selection\"},{\"attributes\":{\"css_classes\":[\"markdown\"],\"margin\":[5,5,5,5],\"name\":\"Markdown02235\",\"text\":\"&lt;h2&gt;Interactive Dashboard&lt;/h2&gt;\"},\"id\":\"1005\",\"type\":\"panel.models.markup.HTML\"},{\"attributes\":{},\"id\":\"1099\",\"type\":\"BasicTickFormatter\"},{\"attributes\":{\"coordinates\":null,\"data_source\":{\"id\":\"1063\"},\"glyph\":{\"id\":\"1065\"},\"group\":null,\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1067\"},\"nonselection_glyph\":{\"id\":\"1066\"},\"selection_glyph\":{\"id\":\"1070\"},\"view\":{\"id\":\"1069\"}},\"id\":\"1068\",\"type\":\"GlyphRenderer\"},{\"attributes\":{},\"id\":\"1110\",\"type\":\"UnionRenderers\"},{\"attributes\":{},\"id\":\"1027\",\"type\":\"SaveTool\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_alpha\":{\"value\":1.0},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":1.0},\"hatch_color\":{\"value\":\"black\"},\"hatch_scale\":{\"value\":12.0},\"hatch_weight\":{\"value\":1.0},\"line_alpha\":{\"value\":1.0},\"line_cap\":{\"value\":\"butt\"},\"line_color\":{\"value\":\"black\"},\"line_dash\":{\"value\":[]},\"line_dash_offset\":{\"value\":0},\"line_join\":{\"value\":\"bevel\"},\"line_width\":{\"value\":1},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1094\",\"type\":\"VBar\"},{\"attributes\":{},\"id\":\"1028\",\"type\":\"PanTool\"},{\"attributes\":{\"source\":{\"id\":\"1087\"}},\"id\":\"1093\",\"type\":\"CDSView\"},{\"attributes\":{},\"id\":\"1029\",\"type\":\"WheelZoomTool\"},{\"attributes\":{\"source\":{\"id\":\"1071\"}},\"id\":\"1077\",\"type\":\"CDSView\"},{\"attributes\":{\"overlay\":{\"id\":\"1032\"}},\"id\":\"1030\",\"type\":\"BoxZoomTool\"},{\"attributes\":{},\"id\":\"1031\",\"type\":\"ResetTool\"},{\"attributes\":{\"coordinates\":null,\"data_source\":{\"id\":\"1039\"},\"glyph\":{\"id\":\"1041\"},\"group\":null,\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1043\"},\"nonselection_glyph\":{\"id\":\"1042\"},\"selection_glyph\":{\"id\":\"1046\"},\"view\":{\"id\":\"1045\"}},\"id\":\"1044\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1073\",\"type\":\"Segment\"},{\"attributes\":{},\"id\":\"1112\",\"type\":\"UnionRenderers\"},{\"attributes\":{\"margin\":[5,10,5,10],\"options\":[\"505CH2\",\"2758\",\"ABC81293\"],\"title\":\"Part Numbers\",\"value\":\"505CH2\"},\"id\":\"1006\",\"type\":\"panel.models.widgets.CustomSelect\"},{\"attributes\":{\"data\":{\"x0\":[\"Labour\",\"Materials\",\"SubContract\",\"Others\",\"Total\"],\"x1\":[\"Labour\",\"Materials\",\"SubContract\",\"Others\",\"Total\"],\"y0\":{\"__ndarray__\":\"AAAAAADAXkAAAAAAAABZQAAAAAAAAFRAAAAAAAAAWUAAAAAAAGB6QA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]},\"y1\":{\"__ndarray__\":\"AAAAAADAZUAAAAAAAABZQAAAAAAAMFVAAAAAAABAWUAAAAAAAFR9QA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]}},\"selected\":{\"id\":\"1113\"},\"selection_policy\":{\"id\":\"1112\"}},\"id\":\"1055\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"data\":{\"Costs_left_parenthesis_right_parenthesis\":{\"__ndarray__\":\"\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[0]},\"index\":{\"__ndarray__\":\"\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[0]}},\"selected\":{\"id\":\"1109\"},\"selection_policy\":{\"id\":\"1108\"}},\"id\":\"1039\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"line_alpha\":{\"value\":0.1},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1066\",\"type\":\"Segment\"},{\"attributes\":{\"children\":[{\"id\":\"1005\"},{\"id\":\"1006\"},{\"id\":\"1007\"}],\"css_classes\":[\"panel-widget-box\"],\"margin\":[5,5,5,5],\"name\":\"WidgetBox02237\"},\"id\":\"1004\",\"type\":\"Column\"},{\"attributes\":{\"source\":{\"id\":\"1063\"}},\"id\":\"1069\",\"type\":\"CDSView\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_alpha\":{\"value\":0.1},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":0.1},\"line_alpha\":{\"value\":0.1},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1090\",\"type\":\"VBar\"},{\"attributes\":{\"coordinates\":null,\"data_source\":{\"id\":\"1087\"},\"glyph\":{\"id\":\"1089\"},\"group\":null,\"hover_glyph\":null,\"muted_glyph\":{\"id\":\"1091\"},\"nonselection_glyph\":{\"id\":\"1090\"},\"selection_glyph\":{\"id\":\"1094\"},\"view\":{\"id\":\"1093\"}},\"id\":\"1092\",\"type\":\"GlyphRenderer\"},{\"attributes\":{\"line_alpha\":{\"value\":0.2},\"x0\":{\"field\":\"x0\"},\"x1\":{\"field\":\"x1\"},\"y0\":{\"field\":\"y0\"},\"y1\":{\"field\":\"y1\"}},\"id\":\"1051\",\"type\":\"Segment\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_alpha\":{\"value\":0.2},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":0.2},\"line_alpha\":{\"value\":0.2},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1083\",\"type\":\"VBar\"},{\"attributes\":{},\"id\":\"1116\",\"type\":\"UnionRenderers\"},{\"attributes\":{\"data\":{\"x0\":[\"Labour\",\"Materials\",\"SubContract\",\"Others\",\"Total\"],\"x1\":[\"Labour\",\"Materials\",\"SubContract\",\"Others\",\"Total\"],\"y0\":{\"__ndarray__\":\"AAAAAABwdEAAAAAAAABZQAAAAAAAwFhAAAAAAAAAWkAAAAAAABiDQA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]},\"y1\":{\"__ndarray__\":\"AAAAAABAcUAAAAAAAABZQAAAAAAAkFdAAAAAAADAWUAAAAAAAJ6BQA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]}},\"selected\":{\"id\":\"1111\"},\"selection_policy\":{\"id\":\"1110\"}},\"id\":\"1047\",\"type\":\"ColumnDataSource\"},{\"attributes\":{\"bottom\":{\"field\":\"bottom\"},\"fill_alpha\":{\"value\":0.1},\"fill_color\":{\"value\":\"#30a2da\"},\"hatch_alpha\":{\"value\":0.1},\"line_alpha\":{\"value\":0.1},\"top\":{\"field\":\"top\"},\"width\":{\"value\":0.7},\"x\":{\"field\":\"index\"}},\"id\":\"1082\",\"type\":\"VBar\"},{\"attributes\":{\"client_comm_id\":\"053b774603b44611bb39f9f87b7dd46e\",\"comm_id\":\"1f7e045b611c41889818e87ecec6f7b8\",\"plot_id\":\"1002\"},\"id\":\"1214\",\"type\":\"panel.models.comm_manager.CommManager\"},{\"attributes\":{\"margin\":[0,0,0,0],\"tabs\":[{\"id\":\"1145\"},{\"id\":\"1147\"}]},\"id\":\"1002\",\"type\":\"panel.models.tabs.Tabs\"},{\"attributes\":{\"fill_color\":{\"value\":\"black\"},\"x\":{\"field\":\"index\"},\"y\":{\"field\":\"Costs_left_parenthesis_right_parenthesis\"}},\"id\":\"1041\",\"type\":\"Circle\"},{\"attributes\":{\"data\":{\"bottom\":{\"__ndarray__\":\"AAAAAAAgbEAAAAAAAABZQAAAAAAAYFZAAAAAAACAWUAAAAAAACSAQA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]},\"index\":[\"Labour\",\"Materials\",\"SubContract\",\"Others\",\"Total\"],\"top\":{\"__ndarray__\":\"AAAAAADAZUAAAAAAAABZQAAAAAAAMFVAAAAAAABAWUAAAAAAAFR9QA==\",\"dtype\":\"float64\",\"order\":\"little\",\"shape\":[5]}},\"selected\":{\"id\":\"1121\"},\"selection_policy\":{\"id\":\"1120\"}},\"id\":\"1087\",\"type\":\"ColumnDataSource\"},{\"attributes\":{},\"id\":\"1117\",\"type\":\"Selection\"},{\"attributes\":{\"children\":[{\"id\":\"1004\"},{\"id\":\"1008\"}],\"margin\":[0,0,0,0],\"name\":\"Costs\"},\"id\":\"1003\",\"type\":\"Row\"},{\"attributes\":{\"margin\":[0,0,0,0],\"name\":\"ManHour Tracking\",\"tags\":[\"hidden\"]},\"id\":\"1146\",\"type\":\"Spacer\"}],\"root_ids\":[\"1002\",\"1214\",\"1281\"]},\"title\":\"Bokeh Application\",\"version\":\"2.4.2\"}};\n",
       "    var render_items = [{\"docid\":\"b21307fa-0cdc-4423-910d-79493b062893\",\"root_ids\":[\"1002\"],\"roots\":{\"1002\":\"5327be2e-7a3f-4199-ab0c-372fd7add62b\"}}];\n",
       "    root.Bokeh.embed.embed_items_notebook(docs_json, render_items);\n",
       "  }\n",
       "  if (root.Bokeh !== undefined && root.Bokeh.Panel !== undefined) {\n",
       "    embed_document(root);\n",
       "  } else {\n",
       "    var attempts = 0;\n",
       "    var timer = setInterval(function(root) {\n",
       "      if (root.Bokeh !== undefined && root.Bokeh.Panel !== undefined) {\n",
       "        clearInterval(timer);\n",
       "        embed_document(root);\n",
       "      } else if (document.readyState == \"complete\") {\n",
       "        attempts++;\n",
       "        if (attempts > 200) {\n",
       "          clearInterval(timer);\n",
       "          console.log(\"Bokeh: ERROR: Unable to run BokehJS code because BokehJS library is missing\");\n",
       "        }\n",
       "      }\n",
       "    }, 25, root)\n",
       "  }\n",
       "})(window);</script>"
      ],
      "text/plain": [
       "Tabs(dynamic=True)\n",
       "    [0] Row(name='Costs')\n",
       "        [0] WidgetBox\n",
       "            [0] Markdown(str)\n",
       "            [1] Select(name='Part Numbers', options=['505CH2', 2758, ...], value='505CH2')\n",
       "            [2] Select(name='Work Required', options=['REP', 'O/H', 'SST'], value='REP')\n",
       "        [1] ParamFunction(function)\n",
       "    [1] Row(name='ManHour Tracking')\n",
       "        [0] WidgetBox\n",
       "            [0] Markdown(str)\n",
       "            [1] Select(name='Part Numbers', options=['505CH2', 2758, ...], value='505CH2')\n",
       "            [2] Select(name='Work Required', options=['REP', 'O/H', 'SST'], value='REP')\n",
       "        [1] Column\n",
       "            [0] ParamFunction(function)\n",
       "        [2] ParamFunction(function)"
      ]
     },
     "execution_count": 3,
     "metadata": {
      "application/vnd.holoviews_exec.v0+json": {
       "id": "1002"
      }
     },
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
    "tabs\n"
   ]
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
