import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trampoline running')
@cli.command()
def start(): click.echo('trampoline started')
if __name__ == '__main__': cli()
