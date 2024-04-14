import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required, ReferenceInput } from 'react-admin';

export const ShippingAddresses_Creat = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user_id" reference='Users'/>
            <TextInput source="recipient_name" multiline={true}/>
            <TextInput source="address_line1"/>
            <TextInput source="address_line2"/>
            <TextInput source="city"/>
            <TextInput source="state"/>
            <TextInput source="postal_code"/>
            <TextInput source="country"/>
        </SimpleForm>
    </Create>
);