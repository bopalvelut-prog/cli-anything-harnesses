import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pfSense running')
@cli.command()
def rules(): click.echo('Firewall rules')
if __name__ == '__main__': cli()
