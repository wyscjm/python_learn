

"""
ctypes type 	C type 									Python type
c_bool 			_Bool 									bool (1)
c_char 			char 									1-character string
c_wchar 		wchar_t 								1-character unicode string
c_byte 			char 									int/long
c_ubyte 		unsigned char 							int/long
c_short 		short 									int/long
c_ushort 		unsigned short 							int/long
c_int 			int 									int/long
c_uint 			unsigned int 							int/long
c_long 			long 									int/long
c_ulong 		unsigned long 							int/long
c_longlong 		__int64 or long long 					int/long
c_ulonglong 	unsigned __int64 or unsigned long long 	int/long
c_float 		float 									float
c_double 		double 									float
c_longdouble 	long double 							float
c_char_p 		char * (NUL terminated) 				string or None
c_wchar_p 		wchar_t * (NUL terminated) 				unicode or None
c_void_p 		void * 									int/long or None
"""

var_maps  ={
		"_Bool 						" : "c_bool				" ,
		"char 						" : "c_char 		   	" ,
		"wchar_t 					" : "c_wchar 	      	" ,
		"char 						" : "c_byte 		  	" ,
		"unsigned char 				" : "c_ubyte 	      	" ,
		"short 						" : "c_short 	      	" ,
		"unsigned short 			" : "c_ushort 	      	" ,
		"int 						" : "c_int 		      	" ,
		"unsigned int 				" : "c_uint 		  	" ,
		"long 						" : "c_long 		  	" ,
		"unsigned long 				" : "c_ulong 	      	" ,
		"__int64				 	" : "c_longlong 	  	" ,
		"long long 					" : "c_longlong 	  	" ,
		"unsigned __int64  			" : "c_ulonglong      	" ,
		"unsigned long long 		" : "c_ulonglong 		" ,
		"float 						" : "c_float 	      	" ,
		"double 					" : "c_double 	      	" ,
	 	"long double 				" : "c_longdouble     	" ,
		"char * (NUL terminated) 	" : "c_char_p 	      	" ,
		"wchar_t * (NUL terminated) " : "c_wchar_p 	      	" ,
		"void * 					" : "c_void_p 	      	" ,
}


def get_mid_string(str,begin_char,end_char):
	try:
		#print begin_char,end_char
		#print str.index(begin_char),str.index(end_char)
		if begin_char and end_char:
			pos_begin = str.index(begin_char)
			pos_end	  = str.index(end_char)
			#print str[int(pos_begin + len(begin_char) + 1):int(pos_end)]
			return str[int(pos_begin + len(begin_char) + 1):int(pos_end)]
	except :
		return None
	


def process_struct(data):
	new_class = "class @1(Structure):\n    _fields_ = [\n@2\n    ]"
	temp = data.split("\n")
	ret = "\"\"\"\n" + data + "\"\"\"\n"
	#print temp[-2]
	#print temp[0]
	#print get_mid_string(temp[-2],"}",";")
	if get_mid_string(temp[-2],"}",";"):		
		var1 = get_mid_string(temp[-2],"}",";")
	else:
		var1 = get_mid_string(temp[0],"struct","{")
	if var1:
		var1 = var1.strip()
		#print new_class.replace("@1",var1)
		new_class = new_class.replace("@1",var1)
		
	var2 = ""
	for line in temp[1:-2]:
		elems = line.split(" ")
		__value = ""
		__key = ""
		if ";" in line:
			for elem in elems:
				if ";" in elem:
					__value = elem.replace(";","")
					#print line
					#print __value
					__key = line[0:line.index(elem)]
		if __value and __key:
			for key in var_maps.keys():
				if key.replace(" ","") == __key.replace(" ",""):				
					__key = key.replace(" ","")
			var2 += "    \"" + __value.strip() + "\": " + __key.strip()  + "\n"
	if var2:
		new_class = new_class.replace("@2",var2)
	#print var2
	ret += new_class
	return ret
	

f_in = open("vxlapi_prepy.py")

out_data = ""
out_data_temp = ""


# replace "//" to "#"
# replace "/*" to """""




for line in f_in:
	if line.startswith("#define XL") or  line.startswith("#define LIN") or line.startswith("#define RECEIVE") :
		line = line.replace("(unsigned int)","").replace("(unsigned short)","").replace("#define ","").replace("(unsigned char)","")
		if "=" not in line:
			a = line.split(" ")
			pos_in = 0
			for elem in a[1:]:
				if elem:
					pos_in = line.index(elem)
					line = line.replace(elem,"= "+elem)
					break
	if line.startswith("typedef"):
		if ";" in line:
			line = "#" + line
			#print line
	out_data_temp += line
f_in.close()


	
lines = out_data_temp.split("\n")
out_data_temp = ""
temp_data = ""
for line in lines:
	line = line + '\n' 
	if temp_data:
		temp_data += line
		if line.startswith("}") and line.strip().endswith(";"):	
			out_data_temp += process_struct(temp_data)
			temp_data = ""
	else:
		if not line.startswith(" ") and not line.startswith("#") and line.strip().endswith("{"):
			temp_data = line
		else:
			out_data_temp += line
	

out_data = out_data_temp	
f_out = open("vxlapi.py","w")
f_out.write(out_data)
f_out.close()
