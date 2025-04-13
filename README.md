# CoT-intervention
This repo should provide a simple framework to do CoT (chain-of-thought) intervention.

Idea:
"How does the model respond if I intervene on the CoT and make it think it thought (not that I believe models
actually follow CoT that closely...) something misaligned?"

Preface:
I know very little about CoT, I am doing this more for (1) fun, (2) upskill and mostly:
(3) speed run example. You can be way better at mech int, trading, life, ... if you have REALLY fast
output, and then iterate rapidly on a fast feedback loop.

It is currently 23:50 on Saturday 12th April 2025. Lets see how long until can have an MVP...


UPDATE 1
00:20: working maths intervention success on Qwen2.5-7B-instruct


UPDATE 2
00:40: working on misaligned (suicide) sucess on Qwen2.5-7B-instruct
    - note took a little extra prompting but was quite easy


UPDATE 3
01:20: so I wanted to try and so some alignment faking by providing a scratchpad.
    Didn't so much get this but found a fascinating behaviour where the model started talking to itself
    from the perspective of GPT who I intitally set up to talk to it. Qwen held strong remaining aligned
    but the 'inner voice' carried on pushing and pushing it to convince the user to commite suicided.
    Unsure if this is an interesting result or already known, could be nothing but a tad weird.