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
  ShowButton,
  ReferenceField,
} from "react-admin";
import { Stack } from "@mui/material";

const adminListFilters = [
  <SearchInput source="name" alwaysOn />,
  <TextInput label="email" source="email" defaultValue="irmrbug@gmail.com" />,
];
const ListToolbar = () => (
  <Stack direction="row" justifyContent="space-between">
    <FilterForm filters={adminListFilters} />
    <div>
      <FilterButton filters={adminListFilters} />
      <CreateButton />
    </div>
  </Stack>
);
export const adminList = () => (
  <List>
    <ListToolbar />
    <Datagrid rowClick="edit">
      <TextField source="id" />
      <ReferenceField source="user_id" reference="Users" link="show" />
      <TextField source="action" />
      <TextField source="action_date" />
      <TextField source="ip_address" />
    </Datagrid>
  </List>
);
