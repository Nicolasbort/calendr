function createItem<T>(key: string, value: Partial<T>): Partial<T> {
  const existingItems = listItems<Partial<T>>(key) || [];
  existingItems.push(value);
  localStorage.setItem(key, JSON.stringify(existingItems));
  return value;
}

function listItems<T>(key: string): T[] {
  const items = localStorage.getItem(key);
  return items ? JSON.parse(items) : [];
}

function getItem<T extends Entity>(key: string, id: string): T | undefined {
  const items = listItems<T>(key);

  return items?.find((item) => item.id === id) || undefined;
}

function updateItem<T extends Entity>(
  key: string,
  id: string,
  updatedValue: Partial<T>
): T[] | undefined {
  const existingItems = listItems<T>(key);

  console.log("existingItems", existingItems);

  if (existingItems) {
    const index = existingItems.findIndex((item) => item.id === id);

    console.log("index", index);
    console.log("ID passado na funcao", id);

    if (index !== -1) {
      const updatedItem = { ...existingItems[index], ...updatedValue };
      existingItems[index] = updatedItem;
      localStorage.setItem(key, JSON.stringify(existingItems));
      return existingItems;
    }
  }

  return undefined;
}

function deleteItem<T extends Entity>(
  key: string,
  id: string
): T[] | undefined {
  const existingItems = listItems<T>(key);

  if (existingItems) {
    const index = existingItems.findIndex((item) => item.id === id);

    if (index !== -1) {
      existingItems.splice(index, 1);
      localStorage.setItem(key, JSON.stringify(existingItems));
      return existingItems;
    }
  }

  return undefined;
}

export { createItem, deleteItem, getItem, listItems, updateItem };
