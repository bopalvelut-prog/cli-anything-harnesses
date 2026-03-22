import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def subscribers(): click.echo('MailerLite subscribers')
@cli.command()
def campaigns(): click.echo('MailerLite campaigns')
if __name__ == '__main__': cli()
