import type { Item } from "~/types"

export const useItemForCart = () => {
    return useState<Item|null>('itemForCart', () => null)
}