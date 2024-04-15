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
)
export const Order_details_list = () => (
    <List>
        <ListToolbar />
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <ReferenceField source="order_id" reference="Orders" link="show" />
            {/* <TextField source="product_id" /> */}
            <TextField source="quantity" />
            <TextField source="unit_price" />
        </Datagrid>
    </List>
);