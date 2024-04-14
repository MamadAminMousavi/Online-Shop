import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required } from 'react-admin';

export const Products_Creat = () => (
    <Create>
        <SimpleForm>
            <TextInput source="name" validate={[required()]} />
            <TextInput source="description" multiline={true}/>
            <TextInput source="category_id"/>
            <TextInput source="picture"/>
        </SimpleForm>
    </Create>
);