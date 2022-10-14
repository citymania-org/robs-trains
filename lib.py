from nml.grfstrings import NewGRFString, default_lang

import grf

class Train(grf.Train):
    pass

set_global_train_y_offset = lambda ofs: grf.ComputeParameters(target=0x8e, operation=0x00, if_undefined=False, source1=0xff, source2=0xff, value=ofs)
