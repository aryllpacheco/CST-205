from PIL import Image


#long_string = '132 139 144 146 142 134 151 153 167 166 136 49 26 21 17 18 24 24 43 39 17 4 2 11 8 3 5 9 7 128 136 135 132 130 132 139 135 168 170 111 39 24 16 14 19 30 40 40 34 16 8 9 9 0 5 3 4 8 126 127 125 125 124 138 158 157 128 93 83 46 18 11 10 11 17 18 25 23 9 5 6 3 5 6 7 10 13 123 125 119 125 130 148 117 46 17 16 15 11 14 14 11 12 11 9 6 5 4 6 6 7 23 64 45 16 8 137 129 124 132 119 47 22 39 63 34 48 83 53 21 11 8 12 9 10 7 6 8 7 21 63 147 160 24 9 129 134 135 89 15 92 162 174 169 63 69 174 175 110 69 43 6 2 2 3 5 15 74 127 162 182 190 63 12 130 143 121 17 46 208 242 207 196 77 57 150 153 126 102 126 73 2 0 2 6 65 144 176 185 173 149 93 17 145 147 62 19 82 227 248 210 211 140 124 128 134 47 42 69 165 23 6 6 36 127 170 190 191 190 200 187 19 158 150 29 11 54 181 225 205 168 28 55 103 98 62 39 49 79 16 20 77 85 135 175 169 186 221 253 223 26 170 146 16 8 25 111 153 136 137 48 86 199 172 142 74 77 37 10 8 39 82 108 149 166 181 212 255 237 41 172 157 20 6 6 33 62 89 121 31 52 194 146 85 71 46 15 9 10 25 68 120 162 182 188 205 239 209 42 161 157 47 9 6 9 19 52 88 25 112 108 59 33 28 17 12 10 16 31 75 131 153 158 156 181 210 124 24 153 158 89 17 11 6 8 17 21 17 34 23 13 10 9 7 10 10 18 36 72 101 110 118 117 110 115 36 11 158 166 151 38 17 14 8 7 9 10 11 12 14 13 13 14 12 11 10 11 27 47 48 44 38 33 46 17 5 162 171 162 134 33 16 11 6 7 9 9 12 13 13 12 12 13 9 4 2 5 6 11 10 11 19 30 4 0 172 163 158 164 155 70 13 6 5 8 6 10 12 11 12 11 10 8 3 2 7 11 12 11 12 42 25 3 1 159 154 152 155 173 180 159 70 34 22 15 14 12 11 11 12 10 6 5 5 8 7 3 2 25 57 9 2 7 152 144 137 143 156 178 152 108 57 36 30 34 46 15 18 19 16 10 7 2 0 4 5 5 33 50 5 1 4'
mona_lisa_string = '''132 139 144 146 142 134 151 153 167 166 136 49 26 21 17 18 24 24 43 39 17 4 2 11 8 3 5 9 7
128 136 135 132 130 132 139 135 168 170 111 39 24 16 14 19 30 40 40 34 16 8 9 9 0 5 3 4 8
126 127 125 125 124 138 158 157 128 93 83 46 18 11 10 11 17 18 25 23 9 5 6 3 5 6 7 10 13
123 125 119 125 130 148 117 46 17 16 15 11 14 14 11 12 11 9 6 5 4 6 6 7 23 64 45 16 8
137 129 124 132 119 47 22 39 63 34 48 83 53 21 11 8 12 9 10 7 6 8 7 21 63 147 160 24 9
129 134 135 89 15 92 162 174 169 63 69 174 175 110 69 43 6 2 2 3 5 15 74 127 162 182 190 63 12
130 143 121 17 46 208 242 207 196 77 57 150 153 126 102 126 73 2 0 2 6 65 144 176 185 173 149 93 17
145 147 62 19 82 227 248 210 211 140 124 128 134 47 42 69 165 23 6 6 36 127 170 190 191 190 200 187 19
158 150 29 11 54 181 225 205 168 28 55 103 98 62 39 49 79 16 20 77 85 135 175 169 186 221 253 223 26
170 146 16 8 25 111 153 136 137 48 86 199 172 142 74 77 37 10 8 39 82 108 149 166 181 212 255 237 41
172 157 20 6 6 33 62 89 121 31 52 194 146 85 71 46 15 9 10 25 68 120 162 182 188 205 239 209 42
161 157 47 9 6 9 19 52 88 25 112 108 59 33 28 17 12 10 16 31 75 131 153 158 156 181 210 124 24
153 158 89 17 11 6 8 17 21 17 34 23 13 10 9 7 10 10 18 36 72 101 110 118 117 110 115 36 11
158 166 151 38 17 14 8 7 9 10 11 12 14 13 13 14 12 11 10 11 27 47 48 44 38 33 46 17 5
162 171 162 134 33 16 11 6 7 9 9 12 13 13 12 12 13 9 4 2 5 6 11 10 11 19 30 4 0
172 163 158 164 155 70 13 6 5 8 6 10 12 11 12 11 10 8 3 2 7 11 12 11 12 42 25 3 1
159 154 152 155 173 180 159 70 34 22 15 14 12 11 11 12 10 6 5 5 8 7 3 2 25 57 9 2 7
152 144 137 143 156 178 152 108 57 36 30 34 46 15 18 19 16 10 7 2 0 4 5 5 33 50 5 1 4'''

img_list = mona_lisa_string.split('\n')
width = len(img_list)
height = len(img_list[0].split())
img = Image.new('L', (width,height))

for x, row in enumerate(img_list):
    for y, el in enumerate(row.split()):
        img.putpixel((x,y), int(el))

img.save('monalisa.png')

img.show()



#was working on trying to read the data from the file to actually
#get the img to populate with the correct grey value but was not 
#able to get it working. So I tried to use a long string to figure it out
#but ran out of time before I was able to get it working  