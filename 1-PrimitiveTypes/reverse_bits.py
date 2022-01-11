pre = {2:1,0:0,1:2,3:3}
def reverse_bits(x):
    mask_size = 2
    bit_mask = 3
    first_16 = pre[x & bit_mask] << 3 * mask_size
    second_16 = pre[(x>>mask_size) & bit_mask] << 2 * mask_size
    third_16 = pre[(x>> 2 * mask_size) & bit_mask] <<mask_size
    final_16 = pre[(x>> 3 * mask_size) & bit_mask]
    return first_16 | second_16 | third_16 | final_16

print(reverse_bits(9)) # 32775
    
