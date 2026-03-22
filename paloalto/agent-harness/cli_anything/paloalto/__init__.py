import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Palo Alto firewall running')
@cli.command()
def rules(): click.echo('Security rules')
if __name__ == '__main__': cli()
