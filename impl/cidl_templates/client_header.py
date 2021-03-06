#
# Copyright 2016, Data61
# Commonwealth Scientific and Industrial Research Organisation (CSIRO)
# ABN 41 687 119 230.
#
# This software may be distributed and modified according to the terms of
# the BSD 2-Clause license. Note that NO WARRANTY is provided.
# See "LICENSE_BSD2.txt" for details.
#
# @TAG(D61_BSD)
#

{{if len(comment_text) > 0}}
    /*{{comment_text}} */\n
{{endif}}

{{py: first = True}}
{{return_type}} {{fname}}(
    {{for type, itype, name, mode, dr, apfx, aref, apsfx in calist}}
        {{if first}}
            {{py: first = False}}
        {{else}}
            , 
        {{endif}}
        {{type}} {{name}}
    {{endfor}}
);
\n
