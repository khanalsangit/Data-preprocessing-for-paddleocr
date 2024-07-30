# copyright (c) 2020 PaddlePaddle Authors. All Rights Reserve.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def gen_rec_label(input_path, out_label):
    with open(out_label, 'w') as out_file:
        with open(input_path, 'r') as f:
            for line in f.readlines():
                tmp = line.strip('\n').split(',')
                img_path, label = tmp[0], tmp[1]
                label = label.replace("\"", "")
                out_file.write(img_path + '\t' + label + '\n')
    out_file.close()           
