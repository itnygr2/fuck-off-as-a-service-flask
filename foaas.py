import os
from flask import Flask,redirect

app = Flask(__name__)

@app.route('/operations') 
def operations(): 
	return redirect('https://www.foaas.com/operations', code=302)

@app.route('/anyway/<company>/<ffrom>') 
def anyway_company_ffrom(company,ffrom): 
	return redirect('https://www.foaas.com/anyway/{company}/{ffrom}', code=302)

@app.route('/asshole/<ffrom>') 
def asshole_ffrom(ffrom): 
	return redirect('https://www.foaas.com/asshole/{ffrom}', code=302)

@app.route('/awesome/<ffrom>') 
def awesome_ffrom(ffrom): 
	return redirect('https://www.foaas.com/awesome/{ffrom}', code=302)

@app.route('/back/<name>/<ffrom>') 
def back_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/back/{name}/{ffrom}', code=302)

@app.route('/bag/<ffrom>') 
def bag_ffrom(ffrom): 
	return redirect('https://www.foaas.com/bag/{ffrom}', code=302)

@app.route('/ballmer/<name>/<company>/<ffrom>') 
def ballmer_name_company_ffrom(name,company,ffrom): 
	return redirect('https://www.foaas.com/ballmer/{name}/{company}/{ffrom}', code=302)

@app.route('/bday/<name>/<ffrom>') 
def bday_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/bday/{name}/{ffrom}', code=302)

@app.route('/because/<ffrom>') 
def because_ffrom(ffrom): 
	return redirect('https://www.foaas.com/because/{ffrom}', code=302)

@app.route('/blackadder/<name>/<ffrom>') 
def blackadder_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/blackadder/{name}/{ffrom}', code=302)

@app.route('/bucket/<ffrom>') 
def bucket_ffrom(ffrom): 
	return redirect('https://www.foaas.com/bucket/{ffrom}', code=302)

@app.route('/bus/<name>/<ffrom>') 
def bus_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/bus/{name}/{ffrom}', code=302)

@app.route('/bm/<name>/<ffrom>') 
def bm_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/bm/{name}/{ffrom}', code=302)

@app.route('/bye/<ffrom>') 
def bye_ffrom(ffrom): 
	return redirect('https://www.foaas.com/bye/{ffrom}', code=302)

@app.route('/caniuse/<tool>/<ffrom>') 
def caniuse_tool_ffrom(tool,ffrom): 
	return redirect('https://www.foaas.com/caniuse/{tool}/{ffrom}', code=302)

@app.route('/chainsaw/<name>/<ffrom>') 
def chainsaw_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/chainsaw/{name}/{ffrom}', code=302)

@app.route('/cocksplat/<name>/<ffrom>') 
def cocksplat_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/cocksplat/{name}/{ffrom}', code=302)

@app.route('/cool/<ffrom>') 
def cool_ffrom(ffrom): 
	return redirect('https://www.foaas.com/cool/{ffrom}', code=302)

@app.route('/cup/<ffrom>') 
def cup_ffrom(ffrom): 
	return redirect('https://www.foaas.com/cup/{ffrom}', code=302)

@app.route('/dalton/<name>/<ffrom>') 
def dalton_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/dalton/{name}/{ffrom}', code=302)

@app.route('/dense/<ffrom>') 
def dense_ffrom(ffrom): 
	return redirect('https://www.foaas.com/dense/{ffrom}', code=302)

@app.route('/deraadt/<name>/<ffrom>') 
def deraadt_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/deraadt/{name}/{ffrom}', code=302)

@app.route('/diabetes/<ffrom>') 
def diabetes_ffrom(ffrom): 
	return redirect('https://www.foaas.com/diabetes/{ffrom}', code=302)

@app.route('/donut/<name>/<ffrom>') 
def donut_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/donut/{name}/{ffrom}', code=302)

@app.route('/dosomething/<do>/<something>/<ffrom>') 
def dosomething_do_something_ffrom(do,something,ffrom): 
	return redirect('https://www.foaas.com/dosomething/{do}/{something}/{ffrom}', code=302)

@app.route('/dumbledore/<ffrom>') 
def dumbledore_ffrom(ffrom): 
	return redirect('https://www.foaas.com/dumbledore/{ffrom}', code=302)

@app.route('/equity/<name>/<ffrom>') 
def equity_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/equity/{name}/{ffrom}', code=302)

@app.route('/even/<ffrom>') 
def even_ffrom(ffrom): 
	return redirect('https://www.foaas.com/even/{ffrom}', code=302)

@app.route('/everyone/<ffrom>') 
def everyone_ffrom(ffrom): 
	return redirect('https://www.foaas.com/everyone/{ffrom}', code=302)

@app.route('/everything/<ffrom>') 
def everything_ffrom(ffrom): 
	return redirect('https://www.foaas.com/everything/{ffrom}', code=302)

@app.route('/family/<ffrom>') 
def family_ffrom(ffrom): 
	return redirect('https://www.foaas.com/family/{ffrom}', code=302)

@app.route('/fascinating/<ffrom>') 
def fascinating_ffrom(ffrom): 
	return redirect('https://www.foaas.com/fascinating/{ffrom}', code=302)

@app.route('/fewer/<name>/<ffrom>') 
def fewer_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/fewer/{name}/{ffrom}', code=302)

@app.route('/field/<name>/<ffrom>/<reference>') 
def field_name_ffrom_reference(name,ffrom,reference): 
	return redirect('https://www.foaas.com/field/{name}/{ffrom}/{reference}', code=302)

@app.route('/flying/<ffrom>') 
def flying_ffrom(ffrom): 
	return redirect('https://www.foaas.com/flying/{ffrom}', code=302)

@app.route('/ftfy/<ffrom>') 
def ftfy_ffrom(ffrom): 
	return redirect('https://www.foaas.com/ftfy/{ffrom}', code=302)

@app.route('/fts/<name>/<ffrom>') 
def fts_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/fts/{name}/{ffrom}', code=302)

@app.route('/fyyff/<ffrom>') 
def fyyff_ffrom(ffrom): 
	return redirect('https://www.foaas.com/fyyff/{ffrom}', code=302)

@app.route('/gfy/<name>/<ffrom>') 
def gfy_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/gfy/{name}/{ffrom}', code=302)

@app.route('/give/<ffrom>') 
def give_ffrom(ffrom): 
	return redirect('https://www.foaas.com/give/{ffrom}', code=302)

@app.route('/greed/<noun>/<ffrom>') 
def greed_noun_ffrom(noun,ffrom): 
	return redirect('https://www.foaas.com/greed/{noun}/{ffrom}', code=302)

@app.route('/holygrail/<ffrom>') 
def holygrail_ffrom(ffrom): 
	return redirect('https://www.foaas.com/holygrail/{ffrom}', code=302)

@app.route('/horse/<ffrom>') 
def horse_ffrom(ffrom): 
	return redirect('https://www.foaas.com/horse/{ffrom}', code=302)

@app.route('/idea/<ffrom>') 
def idea_ffrom(ffrom): 
	return redirect('https://www.foaas.com/idea/{ffrom}', code=302)

@app.route('/immensity/<ffrom>') 
def immensity_ffrom(ffrom): 
	return redirect('https://www.foaas.com/immensity/{ffrom}', code=302)

@app.route('/ing/<name>/<ffrom>') 
def ing_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/ing/{name}/{ffrom}', code=302)

@app.route('/jinglebells/<ffrom>') 
def jinglebells_ffrom(ffrom): 
	return redirect('https://www.foaas.com/jinglebells/{ffrom}', code=302)

@app.route('/keep/<name>/<ffrom>') 
def keep_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/keep/{name}/{ffrom}', code=302)

@app.route('/keepcalm/<reaction>/<ffrom>') 
def keepcalm_reaction_ffrom(reaction,ffrom): 
	return redirect('https://www.foaas.com/keepcalm/{reaction}/{ffrom}', code=302)

@app.route('/king/<name>/<ffrom>') 
def king_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/king/{name}/{ffrom}', code=302)

@app.route('/legend/<name>/<ffrom>') 
def legend_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/legend/{name}/{ffrom}', code=302)

@app.route('/life/<ffrom>') 
def life_ffrom(ffrom): 
	return redirect('https://www.foaas.com/life/{ffrom}', code=302)

@app.route('/linus/<name>/<ffrom>') 
def linus_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/linus/{name}/{ffrom}', code=302)

@app.route('/logs/<ffrom>') 
def logs_ffrom(ffrom): 
	return redirect('https://www.foaas.com/logs/{ffrom}', code=302)

@app.route('/look/<name>/<ffrom>') 
def look_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/look/{name}/{ffrom}', code=302)

@app.route('/looking/<ffrom>') 
def looking_ffrom(ffrom): 
	return redirect('https://www.foaas.com/looking/{ffrom}', code=302)

@app.route('/lowpoly/<ffrom>') 
def lowpoly_ffrom(ffrom): 
	return redirect('https://www.foaas.com/lowpoly/{ffrom}', code=302)

@app.route('/madison/<name>/<ffrom>') 
def madison_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/madison/{name}/{ffrom}', code=302)

@app.route('/maybe/<ffrom>') 
def maybe_ffrom(ffrom): 
	return redirect('https://www.foaas.com/maybe/{ffrom}', code=302)

@app.route('/me/<ffrom>') 
def me_ffrom(ffrom): 
	return redirect('https://www.foaas.com/me/{ffrom}', code=302)

@app.route('/mornin/<ffrom>') 
def mornin_ffrom(ffrom): 
	return redirect('https://www.foaas.com/mornin/{ffrom}', code=302)

@app.route('/no/<ffrom>') 
def no_ffrom(ffrom): 
	return redirect('https://www.foaas.com/no/{ffrom}', code=302)

@app.route('/nugget/<name>/<ffrom>') 
def nugget_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/nugget/{name}/{ffrom}', code=302)

@app.route('/off/<name>/<ffrom>') 
def off_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/off/{name}/{ffrom}', code=302)

@app.route('/off-with/<behavior>/<ffrom>') 
def offwith_behavior_ffrom(behavior,ffrom): 
	return redirect('https://www.foaas.com/off-with/{behavior}/{ffrom}', code=302)

@app.route('/outside/<name>/<ffrom>') 
def outside_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/outside/{name}/{ffrom}', code=302)

@app.route('/particular/<thing>/<ffrom>') 
def particular_thing_ffrom(thing,ffrom): 
	return redirect('https://www.foaas.com/particular/{thing}/{ffrom}', code=302)

@app.route('/pink/<ffrom>') 
def pink_ffrom(ffrom): 
	return redirect('https://www.foaas.com/pink/{ffrom}', code=302)

@app.route('/problem/<name>/<ffrom>') 
def problem_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/problem/{name}/{ffrom}', code=302)

@app.route('/programmer/<ffrom>') 
def programmer_ffrom(ffrom): 
	return redirect('https://www.foaas.com/programmer/{ffrom}', code=302)

@app.route('/pulp/<language>/<ffrom>') 
def pulp_language_ffrom(language,ffrom): 
	return redirect('https://www.foaas.com/pulp/{language}/{ffrom}', code=302)

@app.route('/question/<ffrom>') 
def question_ffrom(ffrom): 
	return redirect('https://www.foaas.com/question/{ffrom}', code=302)

@app.route('/ratsarse/<ffrom>') 
def ratsarse_ffrom(ffrom): 
	return redirect('https://www.foaas.com/ratsarse/{ffrom}', code=302)

@app.route('/retard/<ffrom>') 
def retard_ffrom(ffrom): 
	return redirect('https://www.foaas.com/retard/{ffrom}', code=302)

@app.route('/ridiculous/<ffrom>') 
def ridiculous_ffrom(ffrom): 
	return redirect('https://www.foaas.com/ridiculous/{ffrom}', code=302)

@app.route('/rockstar/<name>/<ffrom>') 
def rockstar_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/rockstar/{name}/{ffrom}', code=302)

@app.route('/rtfm/<ffrom>') 
def rtfm_ffrom(ffrom): 
	return redirect('https://www.foaas.com/rtfm/{ffrom}', code=302)

@app.route('/sake/<ffrom>') 
def sake_ffrom(ffrom): 
	return redirect('https://www.foaas.com/sake/{ffrom}', code=302)

@app.route('/shakespeare/<name>/<ffrom>') 
def shakespeare_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/shakespeare/{name}/{ffrom}', code=302)

@app.route('/shit/<ffrom>') 
def shit_ffrom(ffrom): 
	return redirect('https://www.foaas.com/shit/{ffrom}', code=302)

@app.route('/shutup/<name>/<ffrom>') 
def shutup_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/shutup/{name}/{ffrom}', code=302)

@app.route('/single/<ffrom>') 
def single_ffrom(ffrom): 
	return redirect('https://www.foaas.com/single/{ffrom}', code=302)

@app.route('/thanks/<ffrom>') 
def thanks_ffrom(ffrom): 
	return redirect('https://www.foaas.com/thanks/{ffrom}', code=302)

@app.route('/that/<ffrom>') 
def that_ffrom(ffrom): 
	return redirect('https://www.foaas.com/that/{ffrom}', code=302)

@app.route('/think/<name>/<ffrom>') 
def think_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/think/{name}/{ffrom}', code=302)

@app.route('/thinking/<name>/<ffrom>') 
def thinking_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/thinking/{name}/{ffrom}', code=302)

@app.route('/this/<ffrom>') 
def this_ffrom(ffrom): 
	return redirect('https://www.foaas.com/this/{ffrom}', code=302)

@app.route('/thumbs/<name>/<ffrom>') 
def thumbs_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/thumbs/{name}/{ffrom}', code=302)

@app.route('/too/<ffrom>') 
def too_ffrom(ffrom): 
	return redirect('https://www.foaas.com/too/{ffrom}', code=302)

@app.route('/understand/<name>/<ffrom>') 
def understand_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/understand/{name}/{ffrom}', code=302)

@app.route('/tucker/<ffrom>') 
def tucker_ffrom(ffrom): 
	return redirect('https://www.foaas.com/tucker/{ffrom}', code=302)

@app.route('/waste/<name>/<ffrom>') 
def waste_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/waste/{name}/{ffrom}', code=302)

@app.route('/what/<ffrom>') 
def what_ffrom(ffrom): 
	return redirect('https://www.foaas.com/what/{ffrom}', code=302)

@app.route('/xmas/<name>/<ffrom>') 
def xmas_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/xmas/{name}/{ffrom}', code=302)

@app.route('/yeah/<ffrom>') 
def yeah_ffrom(ffrom): 
	return redirect('https://www.foaas.com/yeah/{ffrom}', code=302)

@app.route('/yoda/<name>/<ffrom>') 
def yoda_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/yoda/{name}/{ffrom}', code=302)

@app.route('/you/<name>/<ffrom>') 
def you_name_ffrom(name,ffrom): 
	return redirect('https://www.foaas.com/you/{name}/{ffrom}', code=302)

@app.route('/zayn/<ffrom>') 
def zayn_ffrom(ffrom): 
	return redirect('https://www.foaas.com/zayn/{ffrom}', code=302)

@app.route('/zero/<ffrom>') 
def zero_ffrom(ffrom): 
	return redirect('https://www.foaas.com/zero/{ffrom}', code=302)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
