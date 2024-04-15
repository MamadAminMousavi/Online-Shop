import * as React from 'react';
import { Create, SimpleForm, TextInput, DateInput, required, ReferenceInput, NumberInput} from 'react-admin';

export const Feedback_Creat = () => (
    <Create>
        <SimpleForm>
            <ReferenceInput source="user_id" reference='Users'/>
            <ReferenceInput source="order_id" reference='Orders'/>
            <NumberInput max={5} min={1} source="rating"/>
            <TextInput source="comment"/>
        </SimpleForm>
    </Create>
);