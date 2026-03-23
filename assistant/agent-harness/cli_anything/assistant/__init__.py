import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('assistant running')
@cli.command()
def start(): click.echo('assistant started')
if __name__ == '__main__': cli()
