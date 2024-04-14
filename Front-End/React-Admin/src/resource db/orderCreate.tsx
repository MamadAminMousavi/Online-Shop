import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required, ReferenceInput } from 'react-admin';

export const OrderCreat = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user_id" reference='Users'/>
            <TextInput source="status"/>
            <TextInput source="total_amount"/>
            {/* <DateInput source="order_date"/> */}
        </SimpleForm>
    </Create>
);