import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def account(): click.echo('Waves account')
@cli.command()
def transfer(): click.echo('Waves transfer')
if __name__ == '__main__': cli()
