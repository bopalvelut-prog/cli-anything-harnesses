import click
@click.group()
def cli(): pass
@cli.command()
def start(): click.echo('AnythingLLM start')
@cli.command()
def chat(): click.echo('AnythingLLM chat')
if __name__ == '__main__': cli()
