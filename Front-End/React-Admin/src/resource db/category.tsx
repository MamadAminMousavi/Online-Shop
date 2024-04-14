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
} from 'react-admin';
import { Stack } from '@mui/material';

const CategoryFilters = [
    <SearchInput source="name" alwaysOn />,
    <TextInput label="email" source="email" defaultValue="irmrbug@gmail.com" />,
];
const ListToolbar = () => (
    <Stack direction="row" justifyContent="space-between">
        <FilterForm filters={CategoryFilters} />
        <div>
            <FilterButton filters={CategoryFilters} />
            <CreateButton />
        </div>
    </Stack>
)
export const CategoryList = () => (
    <List>
        <ListToolbar />
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="name" />
            <TextField source="description" />
            <TextField source="parent_category_id" />
            <DateField source="created_at" />
        </Datagrid>
    </List>
);