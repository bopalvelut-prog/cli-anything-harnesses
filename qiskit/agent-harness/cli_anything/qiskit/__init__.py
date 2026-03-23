import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('qiskit running')
@cli.command()
def start(): click.echo('qiskit started')
if __name__ == '__main__': cli()
