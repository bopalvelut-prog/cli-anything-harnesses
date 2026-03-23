import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_securitycenter running')
@cli.command()
def start(): click.echo('azure_securitycenter started')
if __name__ == '__main__': cli()
