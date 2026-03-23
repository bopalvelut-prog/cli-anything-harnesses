import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('OpenAI chat')
@cli.command()
def models(): click.echo('OpenAI models')
if __name__ == '__main__': cli()
