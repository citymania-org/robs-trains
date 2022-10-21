from nml.grfstrings import NewGRFString, default_lang

import grf

class Train(grf.Train):
    pass

set_global_train_y_offset = lambda ofs: grf.ComputeParameters(target=0x8e, operation=0x00, if_undefined=False, source1=0xff, source2=0xff, value=ofs)

set_global_train_misc_flag = lambda pos: grf.ComputeParameters(target=0x9e, operation=0x08, if_undefined=False, source1=0x9e, source2=0xff, value=1 << pos)
set_global_train_depot_width_32 = lambda: set_global_train_misc_flag(3)
