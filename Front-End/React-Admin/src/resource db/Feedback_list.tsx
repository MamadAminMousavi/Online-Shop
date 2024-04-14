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
    ReferenceField
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
export const Feedback_List = () => (
    <List>
        <ListToolbar />
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <ReferenceField source="user_id" reference="Users" link="show" />
            <ReferenceField source="order_id" reference="Orders" link="show" />
            <TextField source="rating" />
            <TextField source="comment" />
            <DateField source="feedback_date" />
        </Datagrid>
    </List>
);