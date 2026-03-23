import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('llm running')
@cli.command()
def start(): click.echo('llm started')
if __name__ == '__main__': cli()
