import {
    CreateButton,
    Datagrid,
    FilterButton,
    FilterForm,
    ListBase,
    List,
    Pagination,
    TextField,
    TextInput,
    SearchInput,
    EmailField,
    DateField,
  } from "react-admin";
  import { Stack } from "@mui/material";
  
  const Order_detailsFilters = [
    <SearchInput source="name" alwaysOn />,
    <TextInput label="email" source="email" defaultValue="irmrbug@gmail.com" />,
  ];
  const ListToolbar = () => (
    <Stack direction="row" justifyContent="space-between">
      <FilterForm filters={Order_detailsFilters} />
      <div>
        <FilterButton filters={Order_detailsFilters} />
        <CreateButton />
      </div>
    </Stack>
  );
  export const Product_list = () => (
    <List>
      <ListToolbar />
      <Datagrid rowClick="edit">
        <TextField source="product_id" />
        <TextField source="name" />
        <TextField source="description" />
        <TextField source="price" />
        <TextField source="category_id" />
        <TextField source="picture" />
      </Datagrid>
    </List>
  );
  