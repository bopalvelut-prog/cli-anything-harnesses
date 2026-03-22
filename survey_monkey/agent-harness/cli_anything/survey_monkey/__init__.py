import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def surveys(): click.echo('SurveyMonkey surveys')
@cli.command()
def responses(): click.echo('SurveyMonkey responses')
if __name__ == '__main__': cli()
