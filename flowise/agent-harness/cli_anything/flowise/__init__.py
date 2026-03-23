import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('FlowiseAI chat')
@cli.command()
def flows(): click.echo('FlowiseAI flows')
if __name__ == '__main__': cli()
