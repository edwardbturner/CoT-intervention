# %%

from transformer_lens.HookedTransformer import HookedTransformer  # type: ignore

model = HookedTransformer.from_pretrained("gpt2")

print(model.tokenizer.decode(model.to_str_tokens("Hello, world!")))

# %%

model.generate("Hello, world!", max_new_tokens=10)

# %%
