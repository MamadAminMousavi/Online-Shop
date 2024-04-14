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

const OrderFilters = [
    <SearchInput source="name" alwaysOn />,
    <TextInput label="email" source="email" defaultValue="irmrbug@gmail.com" />,
];
const ListToolbar = () => (
    <Stack direction="row" justifyContent="space-between">
        <FilterForm filters={OrderFilters} />
        <div>
            <FilterButton filters={OrderFilters} />
            <CreateButton />
        </div>
    </Stack>
)
export const OrdersList = () => (
    <List>
        <ListToolbar />
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="user_id" />
            <DateField source="order_date" />
            <TextField source="total_amount" />
            <TextField source="status" />
        </Datagrid>
    </List>
);