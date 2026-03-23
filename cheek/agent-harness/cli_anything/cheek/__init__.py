import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cheek running')
@cli.command()
def start(): click.echo('cheek started')
if __name__ == '__main__': cli()
