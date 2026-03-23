import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pizza running')
@cli.command()
def start(): click.echo('pizza started')
if __name__ == '__main__': cli()
