import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Veeam status')
@cli.command()
def backup(): click.echo('Veeam backup')
if __name__ == '__main__': cli()
