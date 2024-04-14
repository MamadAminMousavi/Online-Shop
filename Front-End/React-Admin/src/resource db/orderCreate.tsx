import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const OrderCreat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="user id" validate={[required()]} />
            <TextInput source="status"/>
            <TextInput source="total_amount"/>
            {/* <DateInput source="order_date"/> */}
        </SimpleForm>
    </Create>
);