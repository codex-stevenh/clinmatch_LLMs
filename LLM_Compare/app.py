import gradio as gr
import json

old_prompt = """
           * positive (meaning Patient profile contains the piece of information mentioned in the criterion and it meets this criterion)
           * neutral (meaning more information is needed from the Patient profile to determine if this patient meet the criterion)
           * negative (meaning Patient profile contains the piece of information mentioned in the criteria but it does not meet the criteria)
"""

new_prompt = """
    # Inclusion Criteria   
         * positive (The patient meets the requirement as stated in the inclusion criterion. The patient's profile aligns with the stated conditions or factors. This increases the chances of the patient being admitted into the clinical# trial.)
         * neutral (The patient's profile neither clearly meets nor fails to meet the inclusion criterion. It's possible that some information is missing, not specific enough, or there may be some uncertainty about how well the# patient aligns with the criterion. In this case, further information or tests might be required.)
         * negative (The patient does not meet the requirement as stated in the inclusion criterion. The patient's profile does not align with the conditions or factors stated and hence the patient is not suitable for the clinical# trial.)
    
    # Exclusion Criteria  
         * positive (The patient meets the requirement as stated in the exclusion criterion, meaning the patient has certain conditions or factors that disqualify them from the clinical trial.)
         * neutral (The patient's profile neither clearly meets nor fails to meet the exclusion criterion. It's possible that some information is missing, not specific enough, or there may be some uncertainty about how well the# patient aligns with the criterion. In this case, further information or tests might be required.)
         * negative (The patient does not meet any of the conditions or factors stated in the exclusion criterion. This means none of the disqualifying factors are present in the patient's profile, making them potentially suitable# for the clinical trial.)
"""

def read_local_json(name): 
    
    with open(f'./{name}.json') as f:
        data = json.load(f)

    return data

gpt_35_ = read_local_json('gpt35_vote_result')
llama3_8b_ = read_local_json('llama3_8b_vote_result')

gpt_35_old_ = read_local_json('gpt_old_prompt')
gpt_35_new_ = read_local_json('gpt_new_prompt')

nv_gpt_35_old_ = read_local_json('no_vote_gpt_old_prompt')
nv_gpt_35_new_ = read_local_json('no_vote_gpt_new_prompt')

def gen_comparison(criterion_eva_result, old_eva, new_eva, label_left="Old Prompt Evaluate: ", label_right="New Prompt Evaluate: "):

    with gr.Accordion(f"{criterion_eva_result[0].get('type')} - {criterion_eva_result[0].get('id')}", open=False):
        with gr.Row():
            gr.Textbox(label="Criterion ", value=criterion_eva_result[0].get('criterion', ''), visible=True, lines=5)
        with gr.Row():
            with gr.Column():
                gr.Textbox(label=label_left, value=old_eva, visible=True)
                gr.Textbox(label="Comment: ", value=criterion_eva_result[0].get('comment', ''), visible=True, lines=5)
            with gr.Column():
                gr.Textbox(label=label_right, value=new_eva, visible=True)
                gr.Textbox(label="Comment: ", value=criterion_eva_result[1].get('comment', ''), visible=True, lines=5)
        


with gr.Blocks(theme=gr.themes.Default(primary_hue="blue")) as gradio_app:
    gr.Markdown('# LLM Comparsion')
    
    with gr.Tab("NCT04027647 based patient - no vote"):
        gr.Markdown('## Patient Profile')
        gr.Textbox(label=None, value=f'{gpt_35_old_["patient_profile"]}', show_label=False)

        gr.Markdown('## Prompt')
        gr.Textbox(label=None, value=new_prompt, visible=True, lines=18, show_label=False)

        # with gr.Accordion(f"Comparing Prompts", open=True): 
        #     with gr.Accordion(f"Prompts", open=False):
        #         with gr.Row():
        #             gr.Textbox(label="Old Prompt: ", value=old_prompt, visible=True, lines=8)
        #             gr.Textbox(label="New Prompt: ", value=new_prompt, visible=True, lines=18)


        #     eva_zip_result = zip(gpt_35_old_['evaluate_trials'][0]['criteria'], gpt_35_new_['evaluate_trials'][0]['criteria'])
        #     with gr.Accordion("Result with vote", open=False):

        #         with gr.Tab("Criteria to look at - pos/neg"):

        #             for criterion_eva_result in zip(gpt_35_old_['evaluate_trials'][0]['criteria'], gpt_35_new_['evaluate_trials'][0]['criteria']):

        #                 old_eva = criterion_eva_result[0].get('match_result', '')
        #                 new_eva = criterion_eva_result[1].get('match_result', '')

        #                 if 'neutral' not in [old_eva, new_eva] and old_eva != new_eva:
        #                     gen_comparison(criterion_eva_result, old_eva, new_eva)


        #         with gr.Tab("Criteria to look at - neutral"):

        #             for criterion_eva_result in zip(gpt_35_old_['evaluate_trials'][0]['criteria'], gpt_35_new_['evaluate_trials'][0]['criteria']):

        #                 old_eva = criterion_eva_result[0].get('match_result', '')
        #                 new_eva = criterion_eva_result[1].get('match_result', '')

        #                 if 'neutral' in [old_eva, new_eva] and old_eva != new_eva:

        #                     gen_comparison(criterion_eva_result, old_eva, new_eva)

        #         with gr.Tab("ALL Criteria"):

        #             for criterion_eva_result in zip(gpt_35_old_['evaluate_trials'][0]['criteria'], gpt_35_new_['evaluate_trials'][0]['criteria']):

        #                 gen_comparison(criterion_eva_result, old_eva, new_eva)

        gr.Markdown('## Result')
        with gr.Accordion(f"Comparing LLMs", open=False): 
        
            eva_zip_result = zip(gpt_35_['evaluate_trials'][0]['criteria'], llama3_8b_['evaluate_trials'][0]['criteria'])
    

            with gr.Tab("Click to view - Criteria with opposite evaluaiton result - pos/neg"):
                
                gr.Markdown("### Here are the criteria one LLM gives **Positive** result while the other gives **Negative** result")
                for criterion_eva_result in zip(gpt_35_['evaluate_trials'][0]['criteria'], llama3_8b_['evaluate_trials'][0]['criteria']):

                    old_eva = criterion_eva_result[0].get('match_result', '')
                    new_eva = criterion_eva_result[1].get('match_result', '')

                    if 'neutral' not in [old_eva, new_eva] and old_eva != new_eva:
                        gen_comparison(criterion_eva_result, old_eva, new_eva, "LLM1", "LLM2")


            with gr.Tab("Click to view - Criteria with similar evaluaiton result - neutral"):

                gr.Markdown("### Here are the criteria one LLM gives **Neutral** result while the other gives **Positive/Negative** result")

                for criterion_eva_result in zip(gpt_35_['evaluate_trials'][0]['criteria'], llama3_8b_['evaluate_trials'][0]['criteria']):

                    old_eva = criterion_eva_result[0].get('match_result', '')
                    new_eva = criterion_eva_result[1].get('match_result', '')

                    if 'neutral' in [old_eva, new_eva] and old_eva != new_eva:

                        gen_comparison(criterion_eva_result, old_eva, new_eva, "LLM1", "LLM2")

            with gr.Tab("ALL Criteria"):

                for criterion_eva_result in zip(gpt_35_['evaluate_trials'][0]['criteria'], llama3_8b_['evaluate_trials'][0]['criteria']):

                    gen_comparison(criterion_eva_result, old_eva, new_eva, "LLM1", "LLM2")
               

if __name__ == "__main__":
    # gradio_app.launch(auth=("codex", "codex1234pass"), share=True)
    gradio_app.launch(share=False, server_name="0.0.0.0")